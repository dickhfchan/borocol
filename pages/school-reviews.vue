<template lang="pug">
CardContainer.school-reviews
  .card-container-title School Reviews
  .school.pvl
    .flex
      img.school__avatar(src="https://picsum.photos/100/100?image=406")
      .school__info
        .title2_sm Connect English Language Institute - Mission Vally
        .mtm Address 5090 Shoreham P‘ace‘ sune 206‘ San D‘ego‘ Cahr’orma 92037‘ USA
        .title2_sm.mtl Introduction
        .mtm
          | The umnect Enghsh MAX progvams use an mtenswe mu‘twrskm approach Students acmeve success thvough focused cu57
          | tomwzed attenuon m speakmg‘ hstenmg‘ readmg and vang The Connect Enghsh MAX pvograms mcmde Enghsh gvammav
          | deve‘opment‘ academwc veadmg and wrmng
    Carousel3.school-photos.crousel.mtl(:responsive="[2,3,4,5]")
      .carousel-item(v-for="i in 10" :key="i")
        AspectImage(:src="'https://picsum.photos/250/180?image=6'+i" :aspect="1.5")
  .reviews-total 281 Reviews (Based on Courses)
  form.comment-form.comment
    .comment__left
      img.comment__avatar(src="https://picsum.photos/150/150?image=415")
      .comment__user-name Terry
    .comment__right
      .comment__name English Max Course
      .mtm
        span.mrm Rate your course
        el-rate
      .comment__content
        el-input(type="textarea" :rows="5" placeholder="Share your experience")
        .mts
        el-button.btn3.submit-btn.pull-right(type="primary") Submit
        .clearfix
  .comments.mtl
    .comment.mbm(v-for="i in 5")
      .comment__left
        img.comment__avatar(src="https://picsum.photos/150/150?image=415")
        .comment__user-name Terry
      .comment__right
        div
          span.comment__name English Max Course
          span.comment__daterange May 30 17 , semxo 17
          span.comment__score
            el-rate
        .comment__content Everythmg about thws exbehence was Sensat‘ona‘ Pasca‘ ‘5 hands down the best best we‘ve evev men he‘s \ncredwb kmd and wavm‘ he pxcked us up fvom the ham stench and dropped us offas we“ The abamhem was accurate‘y ve sented by the photos and was dean wnh fresh whens The newghborhood \s a pvetty convement‘ \t‘s
          br
          a.comment__more +More
        .comment__footer.mts
          .comment__date May 30‘ 17
          el-button.btn3.reply-btn(type="primary") Reply
        form.reply-form.justify-sb
          .reply-form-left
            .reply-avatar-wrapper
              img.comment__avatar(src="https://picsum.photos/150/150?image=415")
          .reply-form-right.mlm
            el-input(type="textarea" :rows="5" placeholder="Share your experience")
            el-button.btn3.submit-btn.mtm.pull-right(type="primary") Submit
            .clearfix
    el-pagination.pull-right(:total="50" :page-size="10")
    .clearfix
</template>

<script>
import CardContainer from '@/components/CardContainer'
import Carousel3 from '@/components/Carousel3'

export default {
  components: {CardContainer, Carousel3},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
  },
  beforeDestroy() {
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.school-reviews{
  .container-body{
    @media(max-width: $medium) {
      padding: 0px;
    }
  }
  .el-rate{
    display: inline-block;
  }
  .btn3{
    text-transform: uppercase;
    font-weight: bold;
    padding: 8px 20px;
  }
  //
  .school {

  }
  .school__avatar {
    width: 75px;
    height: 75px;
    border: 1px solid #ccc;
    border-radius: 100%;
    flex-shrink: 0;
    @media(max-width: $small) {
      $side: 50px;
      width: $side;
      height: $side;
    }
  }
  .school__info {
    margin: 10px 0 0 20px;
  }
  .school-photos{
    .item{
    }
    img{
      width: 245px;
    }
  }
  .reviews-total {
    font-size: 22px;
    font-weight: 300;
    margin-top: 40px;
    margin-bottom: 50px;
  }
  .comment{
    display: flex;
    border-bottom: 2px solid #ccc;
    padding-bottom: 15px;
  }
  .comment__avatar{
    $side: 70px;
    width: $side;
    height: $side;
    border-radius: 100%;
    margin-top: 20px;
    @media(max-width: $small) {
      $side: 50px;
      width: $side;
      height: $side;
    }
  }
  .comment__user-name{
    text-align: center;
    font-size: 13px;
    margin-top: 5px;
  }
  .comment__left{
    margin-right: 20px;
  }
  .comment__right{
    flex-grow: 1;
  }
  .comment__name{
    font-size: 16px;
    font-weight: bold;
    margin-right: 20px;
  }
  .comment__daterange{
    font-style: italic;
    margin-right: 30px;
  }
  .comment__score{
  }
  .comment__content{
    margin-top: 15px;
    color: grey;
  }
  .comment__more{
    font-weight: bold;
  }
  .comment__footer{
    text-align: right;
  }
  .comment__date{
    text-align: right;
    font-size: 13px;
    display: inline-block;
  }
  .reply-btn{
    margin-left: 1em;
  }
  .reply-form {
    display: flex;
    margin-top: 10px;
  }
  .reply-form-left {
    width: 100px;
    text-align: right;
  }
  .reply-avatar-wrapper{
    border-left: 1px solid #ccc;
  }
  .reply-form-right {
    flex-grow: 1;
  }
}
</style>
