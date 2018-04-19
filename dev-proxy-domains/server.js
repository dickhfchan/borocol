// proxy domains
var http = require('http'),
    httpProxy = require('http-proxy');

// issue, root is needed if in 3-digit port
// if use other ports like 6666, you may get ERR_UNSAFE_PORT in browser
const port = 8088
//
// Create a proxy server with custom application logic
//
var proxy = httpProxy.createProxyServer({});
proxy.on('error', function(err, req, res){
    res.writeHead(500, {
        'content-type': 'text/plain'
    });
    console.warn(err);
    res.end(err.toString());
});


//
// Create your custom server and just call `proxy.web()` to proxy
// a web request to the target passed in the options
// also you can use `proxy.ws()` to proxy a websockets request
//
var server = http.createServer(function(req, res) {
  // You can define here your custom logic to handle the request
  // and then proxy the request.
  console.log(`${req.method} ${req.url}`);
  req.headers['x-base-url'] = `http://${req.headers.host}`
  if (req.url.startsWith('/api')) {
    proxy.web(req, res, { target: 'http://127.0.0.1:8081' });
  } else {
    proxy.web(req, res, { target: 'http://127.0.0.1:3000' });
  }
});

console.log(`listening on port ${port}`)
server.listen(port);
// request props
// '_readableState',
//   'readable',
//   'domain',
//   '_events',
//   '_eventsCount',
//   '_maxListeners',
//   'socket',
//   'connection',
//   'httpVersionMajor',
//   'httpVersionMinor',
//   'httpVersion',
//   'complete',
//   'headers',
//   'rawHeaders',
//   'trailers',
//   'rawTrailers',
//   'upgrade',
//   'url',
//   'method',
//   'statusCode',
//   'statusMessage',
//   'client',
//   '_consuming',
//   '_dumped'
