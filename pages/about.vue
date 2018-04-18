<template lang="pug">
 .about
  .banner-bar
    .container.container-sm
      .banner-text-area
        .medium-title We envision a world where anyone can save time finding the right program in a foreign country. 
        .medium-title Instead, we do the searching and comparison for you.
        el-button.partner-btn(type="danger") Find Your program now
  .main
    .container.container-sm
      .part2
        .paragraph-title Why host on Borocol?
        el-row.mtl(:gutter="30")
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon.iconimg.book
            .part2-block-title.mtl Licensed Providers
            .part2-block-text.mtl Our host’s legality and trustworthiness have been verified by us.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon.iconimg.bird
            .part2-block-title.mtl Early Bird Discount
            .part2-block-text.mtl Save up to 25% off if you register a program at early stage.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="discount")
            .part2-block-title.mtl Best Price Guarantee
            .part2-block-text.mtl We guarantee you always get the best price when you book a program through us.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon.iconimg.massage
            .part2-block-title.mtl Chat Box
            .part2-block-text.mtl User can simply contact your host via Chat Box in “User Panel” when you got a question concerning your program.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon.iconimg.cancellaction
            .part2-block-title.mtl Cancellation
            .part2-block-text.mtl If you cancel a program “72 hours" within your payment, you will receive a full refund. Cancellation Policy 
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="like")
            .part2-block-title.mtl Authentic Reviews
            .part2-block-text.mtl All reviews are left by real users that are based on their own experiences
          el-col.part2-block(:span="8" :xs="12")
            .paragraph-title For Your Safety
            .part2-block-icon
              Icon.iconimg.safety
            .part2-block-title.mtl Personal ID Safety
            .part2-block-text.mtl “SSL” technology is used in our platform to protect your personal information.
          el-col.part2-block.lock(:span="8" :xs="12")
            .part2-block-icon
              Icon.iconimg.payment
            .part2-block-title.mtl Secure Payment
            .part2-block-text.mtl Pay securely online. We utilize “STRIPE” to collect and transfer payments for you.
            .part2-block-text.mtl (STRIPE supports 135+ currencies and variety of payment. (Visa, MasterCard, American Express, Alipay, Discover, Bitcoin, Wechat pay, JCB, 3DS, ACH Debits, etc.)
          el-col.part2-block(:span="8" :xs="12")
            .paragraph-title Got an issue?
            .part2-block-icon
              Icon.iconimg.support
            .part2-block-title.mtl Customer Support
            .part2-block-text.mtl Our support team is here to assist before, during, or after your experience. Don't hesitate to reach out.

      .part3
        .part3-paragraph
          .part3-left
            .paragraph-title About Borocol
          .part3-right Borocol is a trusted marketplace for host to list, and a platform for people to discover, book and experience across the world. We put people who share the same interest together, participating from a “2-weeks Language Immersion in Seoul” to a “5-Days Yoga Retreat in a luxury resorts at Bali”. With a growing community of users, we promise to keep searching diversified programs to join your journey.
        .part3-paragraph
          .part3-left
            .paragraph-title Our Mission
          .part3-right Make it enjoyable for you to experience a destination offers.
      .part4
        .paragraph-title Key Person
        el-row.key(:gutter="25")
          el-col.mbm.item-center(:sm="12" :xs="24")
            .part4-left.team
              img.docimg(src='https://picsum.photos/200/200?image=111')
            .part4-right.team
              p.docname Dorothy Tse
              p.doclang Spanish / English / Chinese /Indian
              p Borocol is a trusted marketplace for host to list, and a platform for people to discover, book and experience across the world. We put people who share the same interest together,
          el-col.mbm.item-center(:sm="12" :xs="24")
            .part4-left.team
              img.docimg(src='https://picsum.photos/200/200?image=111')
            .part4-right.team
              p.docname Dorothy Tse
              p.doclang Spanish / English / Chinese /Indian
              p Borocol is a trusted marketplace for host to list, and a platform for people to discover, book and experience across the world. We put people who share the same interest together,
          el-col.mbm.item-center(:sm="12" :xs="24")
            .part4-left.team
              img.docimg(src='https://picsum.photos/200/200?image=111')
            .part4-right.team
              p.docname Dorothy Tse
              p.doclang Spanish / English / Chinese /Indian
              p Borocol is a trusted marketplace for host to list, and a platform for people to discover, book and experience across the world. We put people who share the same interest together,
          el-col.mbm.item-center(:sm="12" :xs="24")
            .part4-left.team
              img.docimg(src='https://picsum.photos/200/200?image=111')
            .part4-right.team
              p.docname Dorothy Tse
              p.doclang Spanish / English / Chinese /Indian
              p Borocol is a trusted marketplace for host to list, and a platform for people to discover, book and experience across the world. We put people who share the same interest together,
      .part5
        .paragraph-title Our Team
        el-row.mtl(:gutter="30")
          el-col.p5(:span="12" :xs="24")
            .part3-paragraph.part5-block
              .team-title Web Development:
              img.team-img(src="~assets/img/set.png")
          el-col.p5(:span="12" :xs="24")
            .part3-paragraph.part5-block
              .team-title Design:
              img.team-img(src="~assets/img/blaak.png")




</template>

<script>
import CardContainer from '@/components/CardContainer'

export default {
	layout: 'nomenu',
  components: {CardContainer},
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
	@import "~assets/style/global.scss";
	.about{
	  .banner-bar {
	    background-image: url('~assets/img/partner-banner.jpg');
	    background-size: cover;
	    background-position: center;
	    padding: 85px 0 85px 0;
	  }
	  .banner-text-area {
	    width: 60%;
	    color: rgb(255,255,255);
	    text-align: left;
	  }
	  .big-title {
	    font-weight: bold;
	    font-size: 70px;
	    text-shadow: 0px 3px 15.04px rgb(51, 51, 51);
	  }
	  .medium-title {
	    margin: 50px 0 0 0;
	    font-weight: bold;
	    font-size: 27px;
	    text-shadow: 0px 3px 15.04px rgb(51, 51, 51);
	  }
	  .small-title {
	    font-size: 25px;
	    font-weight: 500;
	    text-shadow: 0px 3px 15.04px rgb(51, 51, 51);
	  }
	  .partner-btn {
	    margin: 50px 0 0 0;
	    font-weight: bold;
	    font-size: 24px;
	    $bg: rgb(255, 82, 103);
	    background: $bg;
	    &:hover{
	      background: darken($bg, 5%);
	    }
	  }
	  .paragraph-title {
	    font-weight: 300;
	    font-size: 38px;
	    text-align: center;
	  }
	  $p1Color: rgb(1,105,109);
	  .paragraph1 {
	    color: $p1Color;
	    font-size: 28px;
	    display: flex;
	    justify-content: space-between;
	    align-items: center;
	    // xs extra small 特小屏幕 手机
	    @media(max-width: $small) {
	      font-size: 18px;
	      .part2-block {
		    min-height: 350px;
		    margin-bottom: 25px;
		   }
	    }
	  }
	  .paragraph1-btn {
	    margin: 0 0 0 15px;
	    font-weight: 500;
	    border: 2px solid $p1Color;
	  }
	  .paragraph2 {
	    margin: 60px 0 0 0;
	  }
	  .paragraph-title2 {
	    font-size: 21px;
	  }
	  .paragraph2-text {
	    font-size: 16px;
	  }
	  .part2 {
	    margin: 125px 0 0 0;
	    text-align: center;
	  }
	  .part2-block {
	    height: 300px;
	    margin-bottom: 25px;
	  }
	  .part2-block-icon {
	    .icon{
	      color: rgb(99,202,206);
	      font-size: 54px;
	    }
	  }
	  .part2-block-title {
	    font-weight: bold;
	    font-size: 24px;
	  }
	  .part2-block-text {
	    font-size: 16px;
	  }
	  .part3-paragraph {
	    min-height: 120px;
	    display: flex; 
	    padding: 0 10px;
	  }
	  .part3-left {
	    width: 400px;
	    font-weight: bold;
	    font-size: 24px;
	    border-right: 1px solid #ccc;
	    flex-shrink: 0;
	  }
	  .part3-right {
	    padding: 0 50px;
	    font-size: 16px;
	    max-width: 600px;
	    line-height: 25px;
	    padding-bottom: 30px;
	  }
	  .part4{
	  	margin-top: 60px;
	  }

	  // xs extra small 特小屏幕 手机
	  @media(max-width: $small) {
	    .part3-paragraph {
	      min-height: auto;
	      display: block;
	      margin-bottom: 20px;
	    }
	    .part3-left {
	      width: auto;
	      font-weight: bold;
	      border-right: none;
	      margin: 0 auto;
	    }
	    .part3-right {
	      padding: 0;
	      max-width: auto;
	      padding-bottom: 0;
	    }
		.part2-block {
		  min-height: 335px !important;
		  margin-bottom: 25px;
		}
		.p5 {
		  text-align: left !important;
		  width: 50%;
		}
		.partner-btn{
		  font-size: 22px;
		}
	   .part2-block-title{
	   	 font-size: 16px;
	   }
	   .part2-block-text{
	   	 font-size: 14px;
	   }
	  }
	   @media(max-width: 600px) {
          .p5{
          	width: 100%;
          }
	   }
	  .iconimg{
	    display: inline-block;
	    width: 100px;
	    height: 58px;
	    background-image: url(~assets/img/icons.png);
	    }
	  .payment{
	    background-position: -445px 75px;
	    height: 75px;

	  }
	  .safety{
	    background-position: 0px 70px;
	  }
	  .cancellaction{
	    background-position: -430px 483px;
	  }
	  .massage{
	    background-position: 0px -266px;
	  }
	  .support{
	    background-position: 100px 60px;
	  }
	  .part3-left.team{
	    width: 100px;
	    border-right: none;
	  }
	  .part3-right.team{
	    padding-left: 20px;
	    padding-right: 0px;
	  }
	  .docimg{
	    width: 100%;
	    border-radius: 100px;
	  }
	  .docname{
	    font-weight: 700;
	  }
	  .doclang{
	    font-size: 12px;
	    color: #999;
	    margin-bottom: 20px;
	  }
	  .part5{
	    width: 65%;
	    margin:0 auto;
	  }
	  .p5{
	  	text-align: center;
	  }
	  .part5-block{
		display: inline-block;
	  }
	  .team-title{
	    font-weight: 700;
	    width: 100%;
	    text-align: left;
	    margin-bottom: 20px;
        font-size: 15px;
    	font-weight: 300;
	  }
	  img.team-img{
	    display: block;
	    width: 100%;
	  }
	  .part2-block {
	    min-height: 250px;
	    margin-bottom: 25px;
	  }



		.el-row {
	    margin-bottom: 20px;
	    &:last-child {
	      margin-bottom: 0;
	    }
	  }
	  .el-col {
	    border-radius: 4px;
	  }
	  .bg-purple-dark {
	    background: #99a9bf;
	  }
	  .bg-purple {
	    background: #d3dce6;
	  }
	  .bg-purple-light {
	    background: #e5e9f2;
	  }
	  .grid-content {
	    border-radius: 4px;
	    min-height: 36px;
	  }
	  .row-bg {
	    padding: 10px 0;
	    background-color: #f9fafc;
	  }
	  .team{
	  	display: inline-block;
	    vertical-align: top;
	    width: 78%;
	  }
	  .part4-left.team{
	  	width: 20%;
        margin-right: 2%;
	  }
	  .key{
	  	margin-top: 50px;
	  }
	  .lock{
	  	margin-top: 30px;
	  	height:350px;
	  }
	  .bird{
	  	background-position: -105px 0px;
	  }
}

</style>
