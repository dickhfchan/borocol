<template lang="pug">
.MainFooter
  ._1
    .container.phn
      .row
        .col-sm-2.col-xs-6
          .title Borocol
          .links
            a.link(href="#") About Us
            a.link(href="#") Recruitment
            a.link(href="#") Media
            a.link(href="#") FAQs
            a.link(href="#") Contact Us
        .col-sm-2.col-xs-6
          .title Contact Us
          .links
            a.link(href="#") Borocol
            a.link(href="#") 103 Arthur Road
            a.link(href="#") Windsor
            a.link(href="#") SL4 1 RU
            a.link(href="#") sales@borocol.com
            a.link(href="#") 01753 833442
        .col-sm-2.col-xs-6
          .title Legal & Cookies
          .links
            a.link(href="#") Terms & Conditions
            a.link(href="#") Privacy Policy
            a.link(href="#") Cookie Policy
            a.link(href="#") Returns Policy
            a.link(href="#")
  ._2
    .container.phn
      span © 2017 All Rights Reserved Borocol - Privacy Policy - Terms and conditions
      .brands
        a(href="#")
          span.icon.icon-facebook
        a(href="#")
          span.icon.icon-linkedin
        a(href="#")
          span.icon.icon-twitter
        a(href="#")
          span.icon.icon-vimeo
        a(href="#")
          span.icon.icon-pinterest
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
@import "~@/assets/css/global.scss";

.MainFooter{
  ._1{
    background-color: #5B5B5D;
    padding-top: 90px;
    padding-bottom: 140px;
    .title{
      color: #fff;
      font-size: 20px;
      font-weight: bold;
    }
    .links{
      margin-top: 10px;
      line-height: 30px;
      a{
        color: #bababa;
        display: block;
      }
    }
  }
  ._2{
    color: #fff;
    font-weight: 500;
    background: #262626;
    padding: 15px 0;
  }
  .brands{
    float: right;
    a{
      display: inline-block;
      color: #fff;
      text-decoration: none;
      margin: 0 10px;
    }
  }
}
</style>
