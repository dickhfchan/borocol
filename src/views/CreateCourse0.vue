<template lang="pug">
.CreateCourse0.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    .container
      .title
        h3 i want to create
      .filter
        .filter_left
          .filter_title A program
            p Accomodation
              span.bold "With"
              span.icon ?
        .or
        .filter_right
          .filter_title A program
            p Accomodation
              span.bold "With"
              span.icon ?
      .text
        ul
          li hereby declare than all information porvide above is true and accurate.
            span.li
          li hereby declare than all information porvide above is true and accurate.
            span.li
      .button
        input(type='button',name='', value='CONFIRM')
</template>

<script>
export default {
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.CreateCourse0{
  *{
  margin: 0px;
  padding: 0px;
  }
  a{
    text-decoration: none;
    color: #63cace;
  }
  ul,ol{
    list-style: none;
  }
  body{
    background: red;
  }
  .container {
    width: 70%;
    height: 700px;
    overflow: hidden;
    margin: 0 auto;
    margin-top: 20px;
    background: #fff;
  }



  /*P1css*/
  .title {
      width: 50%;
      height: 80px;
      margin: 0 auto;
      margin-top: 50px;
      margin-bottom: 32px;
      line-height: 80px;
      text-align: center;
      font-size: 40px;
      color: #464546;
  }
  h3{
        font-weight: lighter;
  }

  .filter {
      width: 60%;
      height: 120px;
      margin: 0 auto;
      position: relative;
  }

  .filter_left {
      position: absolute;
      left: 0px;
      top: 20%;
      width: 43%;
      height: 90px;
      border: solid 2px #a8a2a2;
      border-radius: 3px;
  }
  .filter_title {
    display: block;
    margin: 0 auto;
    margin-top: 20px;
    font-size: 17px;
    text-align: center;
  }
  .filter_left p {
    width: 80%;
    height: 30px;
    margin: 0 auto;
    margin-top: 5px;
    text-align: center;
    font-size: 16px;
  }
  span.bold {
      font-weight: bold;
  }
  .filter_right {
      position: absolute;
      right: 0px;
      top: 20%;
      width: 42%;
      height: 90px;
      border: solid 2px #a8a2a2;
      border-radius: 3px;
  }
  .filter_right p {
    width: 80%;
    height: 30px;
    margin: 0 auto;
    margin-top: 5px;
    text-align: center;
    font-size: 16px;
  }

  .or {
      position: absolute;
      left: 47%;
      top: 33%;
      font-size: 35px;
      color: #5f5f5f;
  }
  .text {
      width: 90%;
      margin-left: 20%;
      margin-top: 30px;
      vertical-align: center;
  }
  .text ul {
      font-size: 14px;
  }
  input[type="button"] {
      width: 100px;
      height: 45px;
      margin: 0 auto;
      margin-top: 30px;
      background: #63cace;
      border: none;
      border-radius: 5px;
      color: #fff;
      font-size: 16px;
      text-align: center;
  }

  .button {
      width: 100px;
      height: 60px;
      margin: 0 auto;
      margin-top: 20px;
      margin-bottom: 100px;
  }
  span.li{
    display: inline-block;
    margin-right: 5px;
    width: 7px;
    height: 7px;
    border-radius: 47px;
    background: #63cace;
    float: left;
  }


}
</style>
