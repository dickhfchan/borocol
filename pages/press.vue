<template lang="pug">
CardContainer.press-page
 .press
  .miantitle Press Release
  .article
    img(src='https://picsum.photos/800/800?image=520')
    h4 Title of the Post
    .small-title Aug 30,2017
    .content
      p
        | The Connect English MAX programs use an intensive, multi-skill approach. Students achieve success through focused, customized attention in speaking, listening, reading and writing. The Connect English MAX programs include English grammar development, academic reading and writing, real-world media projects, and planned social interaction events that are tailored to adult learners’ needs and interests.
      p
        | The Connect English MAX programs use an intensive, multi-skill approach. Students achieve success through focused, customized attention in speaking, listening, reading and writing. The Connect English MAX programs include English grammar development, academic reading and writing, real-world media projects, and planned social interaction events that are tailored to adult learners’ needs and interests.
      p
        | The Connect English MAX programs use an intensive, multi-skill approach. Students achieve success through focused, customized attention in speaking, listening, reading and writing. The Connect English MAX programs include English grammar development, academic reading and writing, real-world media projects, and planned social interaction events that are tailored to adult learners’ needs and interests.
  .hr
  .article
    img(src='https://picsum.photos/800/800?image=399')
    h4 Title of the Post
    .small-title Aug 30,2017
    .content
      p
        | The Connect English MAX programs use an intensive, multi-skill approach. Students achieve success through focused, customized attention in speaking, listening, reading and writing. The Connect English MAX programs include English grammar development, academic reading and writing, real-world media projects, and planned social interaction events that are tailored to adult learners’ needs and interests.
      p
        | The Connect English MAX programs use an intensive, multi-skill approach. Students achieve success through focused, customized attention in speaking, listening, reading and writing. The Connect English MAX programs include English grammar development, academic reading and writing, real-world media projects, and planned social interaction events that are tailored to adult learners’ needs and interests.
      p
        | The Connect English MAX programs use an intensive, multi-skill approach. Students achieve success through focused, customized attention in speaking, listening, reading and writing. The Connect English MAX programs include English grammar development, academic reading and writing, real-world media projects, and planned social interaction events that are tailored to adult learners’ needs and interests.
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
.press-page{
	@import "~assets/style/global.scss";
	.press{
		margin: 0 auto;
		background: #fff;
		padding: 0 12%;
		position:  relative;
		.miantitle{
		font-size: 24px;
		text-align: center;
		padding: 80px 0px 0px 0px;
		}
		h4{
			text-align: center;
			margin-top: 40px;
		}
		.small-title{
			text-align: center;
		}
		.article{
			margin-top: 60px;
			margin-bottom: 60px;
			padding-bottom: 60px;
		}
		.article img{
		    width: 100%;
		}
		.content p{
		    margin-top: 30px;
		    font-size: 14px;
		}
		.hr{
			width: 114%;
			background: #767676;
			position:  relative;
			left: -7%;
			height: 2px;
		}
		.top {
		    font-size: 16px;
		    text-align: center;
		    padding: 5px 20px;
		    color: #fff;
		    background: #b1b1b1;
		    position: absolute;
		    right: 5%;
		    bottom: -2%;
		}
		 // xs extra small 特小屏幕 手机
	    @media(max-width: $small) {
		    .article {
			    margin-top: 30px;
			    margin-bottom: 60px;
			    padding-bottom: 0px;
			}
			.miantitle{
				padding-top: 30px;
			}
	  }
	}
}
</style>
