<template lang="pug">
CardContainer.career-page
 .career
  .article
    .miantitle Career Opportunities
    h2.second Career Vacancies
    h2 Client Services Representative
    h4.city London
    .small-title Aug 30,2017
    .content
      p
        | Overseeing all aspects of Client Services duties within the company (assisting both internal and external clients as well as Phillips specialists)

      p
        | Holding in-depth knowledge of Phillips practices and departments in order to field phone calls via switchboard and introduce clients, visitors and contractors to the gallery to Executives, Specialists and/or Operational staff.

      p.not-top
        | Assisting clients with all aspects of the pre and post-sale auction process including but not limited to; auction registration, condition reports, queries regarding conditions of sale (Buyers’ Premium, catalogue symbols, VAT etc.) and payment and collection, referring them to the relevant department when necessary.
  .article
    h4 Duties And Responsibilities
    ul.content-list
      li
        | Overseeing all aspects of Client Services duties within the company (assisting both internal and external clients as well as Phillips specialists)
      li
        | Holding in-depth knowledge of Phillips practices and departments in order to field phone calls via switchboard and introduce clients, visitors and contractors to the gallery to Executives, Specialists and/or Operational staff.
      li
        | Assisting clients with all aspects of the pre and post-sale auction process including but not limited to; auction registration, condition reports, queries regarding conditions of sale (Buyers' Premium, catalogue symbols, VAT etc.) and payment and callection, referring them to the relevant department when necessary.
      li
        | Assisting the Catalogue Department with distribution and selling of catalogues. 

      li
        | Liaise with the Events Department in managing RSVP lists for previews and events and assist with set up during such events.
      li
        | Support the office in organisation of international and local mail, courier services and deliveries.
        
      li| Ensure all public areas, galleries and meeting rooms are set up to a consistently high standard. 
  .apply APPLY NOW
  .hr
  .top Top

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
.career-page{
	@import "~assets/style/global.scss";
	.career{
		margin: 0 auto;
		background: #fff;
		margin: 5% 8%;
		padding: 0px 10% 0px 10%;
		position:  relative;
		padding-bottom: 100px;
		.miantitle{
			font-size: 50px;
			text-align: center;
			padding: 80px 0px 40px 0px;
			font-weight: 300;
		}
		h4{
			text-align: left;
			margin-top: 40px;
			margin-bottom: 30px;
			font-size: 21px;
		}
		.small-title{
			margin-top:10px;
		}
		.article{
			margin-top: 40px;
			margin-bottom: 40px;
		}
		.article img{
		    width: 100%;
		}
		.content p{
		    margin-top: 30px;
		    font-size: 14px;
		}
		.hr{
			width: 100%;
			background: #767676;
			position:  relative;
			left: 0;
			height: 2px;
		}
		.top {
		    font-size: 16px;
		    text-align: center;
		    padding: 5px 20px;
		    color: #fff;
		    background: #b1b1b1;
		    position: absolute;
		    right: 0%;
		    bottom: 30px;
		}
		.content-list {
			width: 75%;
	    	margin-left: -25px;
		}
		.content-list li{
			margin-top: 30px;
		}
		.apply{
	        width: 60%;
			max-width: 150px;
			padding: 10px 15px;
			font-size: 16px;
			text-align: center;
			background: #48cccd;
			color: #fff;
			border-radius: 3px;
			margin-bottom: 40px;
		}
		.city{
			font-size: 24px;
			margin: 0px;
		}
		h2{
			font-size: 30px;
			font-weight: 700;
		}
		h2.second{
		    margin-bottom: 40px;
		    margin-left: -10px;
		}
		.not-top{
			margin-top: 0px !important;
		}
	}
	// xs extra small 特小屏幕 手机
		@media(max-width: $small) {
			.career {
				    padding: 0;
				    margin: 50px 8%;
			.apply {
				width: 100%;
			}
			.content-list {
				width: 115%;
			}
			.miantitle {
				font-size: 32px;
				padding: 0px 0px 40px 0px;
			}
			h2{
			   font-size: 26px;
			}
			.city{
				font-size: 20px;
			}
			.top{
				right: -25px;
    			bottom: -50px;
			}
		}
	}
}
</style>
