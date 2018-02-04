'use strict'
require('./check-versions')()

process.env.NODE_ENV = 'production'

const ora = require('ora')
const rm = require('rimraf')
const path = require('path')
const chalk = require('chalk')
const webpack = require('webpack')
const config = require('../config')
const webpackConfig = require('./webpack.prod.conf')
const {execSync} = require('child_process');
const dirTree = require('directory-tree');
const {forIn} = require('tree-helper');
const fs = require('fs');

const spinner = ora('building for production...')
spinner.start()

rm(path.join(config.build.assetsRoot, config.build.assetsSubDirectory), err => {
  if (err) throw err
  webpack(webpackConfig, (err, stats) => {
    spinner.stop()
    if (err) throw err
    process.stdout.write(stats.toString({
      colors: true,
      modules: false,
      children: false, // if you are using ts-loader, setting this to true will make tyescript errors show up during build
      chunks: false,
      chunkModules: false
    }) + '\n\n')

    if (stats.hasErrors()) {
      console.log(chalk.red('  Build failed with errors.\n'))
      process.exit(1)
    }

    console.log(chalk.cyan('  Build complete.\n'))
    console.log(chalk.yellow(
      '  Tip: built files are meant to be served over an HTTP server.\n' +
      '  Opening index.html over file:// won\'t work.\n'
    ))
    // start move files to server
    execSync(`rm server/static -r`)
    execSync(`cp dist/static server/static -r`)
    dirTree('./dist', {extensions:/\.html$/}, tree => {
      forIn(tree, item => {
        let name = path.basename(path.dirname(item.path))
        if (name !== 'dist') {
          // move splited scripts append to body
          const str = fs.readFileSync(item.path).toString()
          const head = str.match(/<head[\s\S]*?<\/head>/)[0]
          let scriptsPlaceholderFollow = head.match(/<meta name="scriptsPlaceholder"[\s\S]*$/)[0]
          let scripts = scriptsPlaceholderFollow.match(/<script[\s\S]*?<\/script>/g)
          let head2 = head
          scripts.forEach(s => {
            head2 = head2.replace(s, '')
          })
          const html = str.replace(head, head2).replace(/(<\/body>)/, scripts.join('') + '$1')
          fs.writeFileSync(item.path, html)
          // move to server dir
          name += '.html'
          execSync(`cp ${item.path} server/templates/${name}`)
        }
      })
    })
    execSync(`cp dist/index.html server/templates/spa.html`)
    console.log('successfully moved to server dir');
  })
})
