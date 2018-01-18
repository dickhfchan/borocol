<template lang="pug">
.CreateCourse.container
  router-view
</template>

<script>
import {strRand, arrayLast} from 'helper-js'

export default {
  // components: {},
  data() {
    return {
      state: this.$state.createCourse,
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  created() {
    this.$state.createCourseVm = this
  },
  mounted() {
    window.createCourse = {
      fill: () => {
        const kv = {
          declared: true,
          agreed: true,
          startDate: '2018-01-12',
          endDate: '2018-01-13',
          groupSize: 3,
          gender: 'female',
          hours: 20,
          photos: ['xxx', 'xxx2'],
          seats: 60,
          price: 300.99,
          registrationStartDate: '2018-01-12',
          registrationEndDate: '2018-01-13',
        }
        for (const page of this.state.fields) {
          for (const key in page) {
            const fld = page[key]
            if (kv.hasOwnProperty(key)) {
              this.$set(fld, 'value', kv[key])
            } else if (fld.value == null && fld.rules && fld.rules.match(/required(?!If)/)) {
              this.$set(fld, 'value', strRand(5))
            }
          }
        }
        setTimeout(() => {
          this.$router.push(arrayLast(this.state.routes))
        }, 500);
      },
    }
  },
  beforeDestroy() {
    this.state.validations.forEach(item => {
      item.clear && item.clear()
    })
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCourse{
  .content-card{
    padding: 0;
  }
  .content-card-body.has-tips{
    display: flex;
    justify-content: space-between;
    > form{
      width: 100%;
    }
    .Tips{
      margin-left: 50px;
      flex-shrink: 0;
      margin-bottom: 15px;
    }
  }

  .content-card-header{
    font-size: $fs-title;
    $h: 80px;
    height: $h;
    line-height: $h;
    .step{
      display: inline-block;
      font-weight: bold;
      width: 170px;
      text-align: center;
      color: #1aa7ac;
      border-right: 2px solid $bd1;
    }
    .title{
      display: inline-block;
      padding-left: 30px;
    }
  }
  .content-card-progress-bar{
    background-color: #dbdbdb;
    box-shadow: none;
    border-radius: 0;
    .progress-bar-warning{
      box-shadow: none;
      font-size: 14px;
      color: $color1;
      font-weight: 500;
      background-color: #ffcc00;
    }
  }
  .content-card-body{
    padding: 50px 100px 120px 100px;
    box-sizing: content-box;
  }
  .dividing-line-title{
    .title{
      font-size: $fs-title * 0.8;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 20px 0;
      .line{
        height: 1px;
        width: 35%;
        background: $bd1;
      }
    }
    input, select{
      display: inline-block;
      width: auto;
    }
    .line1{
      select{
        width: 95px;
      }
    }
    .icon{
      color: #ccc;
      font-size: 1.4em;
    }
  }
}
</style>
