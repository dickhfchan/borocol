<template lang="pug">
include ../common.pug
.SchoolReviews
  .container
    .content-card
      h1.content-card-title School Reviews
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
        .school-photos.crousel.mtl
          .item
            img(src="https://picsum.photos/220/150?image=406")
          .item
            img(src="https://picsum.photos/220/150?image=407")
          .item
            img(src="https://picsum.photos/220/150?image=408")
          .item
            img(src="https://picsum.photos/220/150?image=409")
          .item
            img(src="https://picsum.photos/220/150?image=410")
          .item
            img(src="https://picsum.photos/220/150?image=411")
          .item
            img(src="https://picsum.photos/220/150?image=412")
          .item
            img(src="https://picsum.photos/220/150?image=413")
      .reviews-total 281 Reviews (Based on Courses)
      form.comment-form.comment
        .comment__left
          img.comment__avatar(src="https://picsum.photos/150/150?image=415")
          .comment__user-name Terry
        .comment__right
          .comment__name English Max Course
          .mtm Rate your course
            StarScore.mlm
          .comment__content
            +textarea(placeholder="Share your experience" rows="5")
            button.submit-btn.btn.btn-primary.mtm.pull-right Submit
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
                StarScore
            .comment__content Everythmg about thws exbehence was Sensat‘ona‘ Pasca‘ ‘5 hands down the best best we‘ve evev men he‘s \ncredwb kmd and wavm‘ he pxcked us up fvom the ham stench and dropped us offas we“ The abamhem was accurate‘y ve sented by the photos and was dean wnh fresh whens The newghborhood \s a pvetty convement‘ \t‘s
              br
              a.comment__more +More
            .comment__footer.mts
              .comment__date May 30‘ 17
              button.btn3.reply-btn.btn.btn-primary Reply
            form.reply-form.justify-sb
              .reply-form-left
                .reply-avatar-wrapper
                  img.comment__avatar(src="https://picsum.photos/150/150?image=415")
              .reply-form-right.mlm
                +textarea(placeholder="Share your experience" rows="5")
                button.btn3.submit-btn.btn.btn-primary.mtm.pull-right Submit
                .clearfix
        ul.pagination.b.pull-right
          li.disabled
            a(href='#', aria-label='Previous')
              span(aria-hidden='true') «
          li.active
            a(href='#')
              | 1
              span.sr-only (current)
          li
            a(href='#') 2
          li
            a(href='#') 3
          li
            a(href='#') 4
          li
            a(href='#') 5
          li
            a(href='#', aria-label='Next')
              span(aria-hidden='true') »
        .clearfix
</template>

<script>
import 'slick-carousel/slick/slick.css'
import 'slick-carousel/slick/slick'
export default {
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    $(this.$el).find('.crousel').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
      arrows: false,
      dots: true,
    });
  },
  beforeDestroy() {
    $(this.$el).find('.crousel').slick('unslick')
  },
}
</script>

<style lang="scss">
.SchoolReviews{
  .btn3{
    text-transform: uppercase;
    font-weight: bold;
    padding: 5px 20px;
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
  }
  .comment__daterange{
    font-style: italic;
    margin-left: 20px;
  }
  .comment__score{
    margin-left: 30px;
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
