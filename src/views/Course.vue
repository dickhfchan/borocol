<template lang="pug">
include ../common.pug
.Course
  .container
    .breadcrumb
      li
        a(href="javascript:void(0)") Home
      li.active Search Result
    .flex.justify-sb
      .card2_left-wrapper
        .card2.card2_left
          .card2__title Tony Vega class
          .card2__body
            .title2 5 Days Yoga Retreat in a luxury 5 Stars Resort, Okinawa
            .flex
              .instructors-info
                .title3.mbm Your Instructor / Host
                img.instructor-photo.mbl(src="https://picsum.photos/160/115?image=400")
                .instructor-footer
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=401")
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=402")
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=403")
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=404")
                  span.instructor-number
                    span.icon.icon-plus
                    | 10
              .course-detail.mll
                .flex
                  .key Date:
                  .value Jun ‘75, 20‘s
                .flex.mts
                  .key Age Range:
                  .value 18-22
                .flex.mts
                  .key Level:
                  .value All
                .flex.mts
                  .key Location:
                  .value
                    | A560 A‘varado Canyon Road‘ Smte 25‘ E.
                    img.google-map-icon.mlm(src="~@/assets/img/google-map2.png")
                    br
                    | San Dwego‘ Cahforma 92120 USA
                .flex.mts
                  .key Description:
                  .value
                    | Lovem \psum \5 s‘mp‘y dummy textof the pvmtmg and typesemng \ndustry.
                    | Lovem \psum has been the \ndustry's standard dummy text ever s‘noe the
                    | ‘5005, when an unknown pnnter took a gaHey.,.
                .meta
                  .views 40 Views
                  span.collect.collected.icon.icon-heart.mlm(title="Collect / Uncollect")
                  button.share-btn.btn.btn-primary.btn-sm.btn-block.mts
                    span.icon.icon-share.mrs
                    | Share
            Tabs.mtm(v-model="activeTab" styleName="2" :lazy="false")
              Tab(name="General Details")
                el-row.general-detail(:gutter="100")
                  el-col(:span="8")
                    .general-detail__paragraph
                      .general-detail__key Offered in
                      .general-detail__value Engush, Japanese, Ch‘nese
                    .general-detail__paragraph
                      .general-detail__key Duration
                      .general-detail__value 5 Days/ 4 nghls
                    .general-detail__paragraph
                      .general-detail__key Group Size
                      .general-detail__value Mam
                    .general-detail__paragraph
                      .general-detail__key Number of Hours
                      .general-detail__value 95
                    .general-detail__paragraph
                      .general-detail__key Accomodation
                      .general-detail__value \ncmded
                    .general-detail__paragraph
                      .general-detail__key Registration End-Day
                      .general-detail__value May 26, 2018
                    button.send-btn.btn.btn-primary.btn-md
                      span.icon.icon-talk
                      span  Send Inquiry
                  el-col(:span="16")
                    .general-detail__paragraph
                      .general-detail__key Waht We’ll Do
                      .general-detail__value Baswc Know‘edge of programmmg PHD/Javascnpt
                    .general-detail__paragraph
                      .general-detail__key Where We’ll Be
                      .general-detail__value Lorem \psum \s swmp‘y dummy text of the prmtmg and typesettmg
                    .general-detail__paragraph
                      .general-detail__key Itinerary / Typical Daily Schedule
                      .general-detail__value
                        | Momma sess‘on
                        | Break
                        |
                        | Momma sess‘on
                        | Break
                        |
                        | Aftemoon sess‘on
                        |
                        | 09:00 AM 4015 AM
                        | ms AM , ‘0235 AM
                        | ‘0235 AM , m0 AM
                        | uon AM , am PM
                        | mo PM , 0‘25 PM
                    .general-detail__paragraph
                      .general-detail__key What We Will Provide
                      .general-detail__value
                        | Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg mausr
                        | try Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg my
                        | dustry
                    .general-detail__paragraph
                      .general-detail__key What You Need to Bring
                      .general-detail__value
                        | Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg mausr
                        | try Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg my
                        | dustry
                    .general-detail__paragraph
                      .general-detail__key Guest Requirements
                      .general-detail__value
                        | Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg mausr
                        | try Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg my
                        | dustry
                    .general-detail__paragraph
                      .general-detail__key Are Meals Included
                      .general-detail__value Yes Breakfast, Lunch, Dmner
                    .general-detail__paragraph
                      .general-detail__key Can You Obtain a Certi 'cate
                      .general-detail__value Yes
                    .general-detail__paragraph
                      .general-detail__key How to Get There
                      .general-detail__value
                        | Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg mausr
                        | try Lorem \psum \s swmp‘y dummy text of me prmtmg and typesettmg my
                        | dustry
                    .general-detail__paragraph
                      .general-detail__key Notes
                      .general-detail__value You W take a p‘acement test on your ﬁrst day to determme your dass
              Tab(name="About Your Host / Provider")
                .host-provider.pym
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
                        .comment__date May 30‘ 17
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

              Tab(name="Accomodation")
                .accomodation
                  .accomodation-photos.crousel
                    .accomodation-photo-wrapper
                      img(src="https://picsum.photos/220/150?image=416")
                    .accomodation-photo-wrapper
                      img(src="https://picsum.photos/220/150?image=417")
                    .accomodation-photo-wrapper
                      img(src="https://picsum.photos/220/150?image=418")
                    .accomodation-photo-wrapper
                      img(src="https://picsum.photos/220/150?image=419")
                    .accomodation-photo-wrapper
                      img(src="https://picsum.photos/220/150?image=420")
                    .accomodation-photo-wrapper
                      img(src="https://picsum.photos/220/150?image=421")
                  .accomodation-line.mtl
                    .accomodation-key Options
                    .accomodation-value
                      .accomodation-option
                        span.icon.icon-house
                        .mts Dorm
                  .accomodation-line
                    .accomodation-key About the location:
                    .accomodation-value Lorem \psum ‘5 swmp‘y dummy text or’ the prmtmg and typesemng \ndustry
                      br
                      | Lorem \psum has been the mdustry‘s standard dummy text ever smce the
                  .accomodation-line
                    .accomodation-key Facilities:
                    .accomodation-value Wm / mtchen / Swwmmmg poo‘ / Washmg machme/ gym / ba‘cony
                      br
                      | Othevs warary‘ garden
        .advertisement.flex.mtl
          a(href="javascript:void(0)")
            img(src="https://picsum.photos/500/220?image=405")
          a(href="javascript:void(0)")
            img(src="https://picsum.photos/500/220?image=406")
        .related-title.mtl You might be interested in
        el-row(:gutter="16").related.mtl
          el-col(:span="12")
            .course-card
              a.course-card__img-area(href="#")
                img.img(src="https://picsum.photos/500/300?image=407")
                .mark Early Bird Sale
                .course-card__collect.collected
                  span.icon.icon-heart
                .course-card__meta.flex.justify-sb.align-c
                  div
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=401")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=402")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=403")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=404")
                    span.instructor-more
                      span.icon.icon-plus
                      | More
                  span 1000 Views
              .course-card__text-area
                .course-card__title English Max Course
                .course-card__address.mtm SAN D‘EGO, USA
                .flex.justify-sb.mts
                  .course-card__date Feb 20,16 , Mar 30,17
                  .course-card__price USD 600,000
          el-col(:span="12")
            .course-card
              a.course-card__img-area(href="#")
                img.img(src="https://picsum.photos/500/300?image=407")
                .mark Early Bird Sale
                .course-card__collect
                  span.icon.icon-heart-o
                .course-card__meta.flex.justify-sb.align-c
                  div
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=401")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=402")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=403")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=404")
                    span.instructor-more
                      span.icon.icon-plus
                      | More
                  span 1000 Views
              .course-card__text-area
                .course-card__title English Max Course
                .course-card__address.mtm SAN D‘EGO, USA
                .flex.justify-sb.mts
                  .course-card__date Feb 20,16 , Mar 30,17
                  .course-card__price USD 600,000
      div
        .card2_right.card2
          .card2__title
            span.icon.icon-user
            | 5 SPACES LEFT
          .card2__body
            .title2_sm English Max Course
            .date-range.mtm
              span.icon.icon-calendar
              |  Dec 20, 16 - Mar 30,17
            .room.flex.relative.mtm
              Checkbox
              .room__info
                .room__price USD 2,000
                .room__oprice
                  | Orignal
                  span.number USD 2,300
                .room__type Single Room
              .room__early-bird EARLY BIRD
            .room.flex.relative.mts
              Checkbox
              .room__info
                .room__price USD 1,800
                .room__oprice
                  | Orignal
                  span.number USD 2,300
                .room__type Shared Room
              .room__early-bird EARLY BIRD
            .additional.mtm
              .additional__line
              .additional__text Additional
              .additional__line
            .flex.justify-sb.mtm
              div
                Checkbox
                span  Down Payment
              span.question-circle.icon.icon-question-circle
            .price-line.flex.justify-sb.mtm
              span.price-key Program Fee
              span.price-number USD 1,800
            .price-line.flex.justify-sb
              span.price-key  Down Payment
              span.price-number USD 480
            .price-total.flex.justify-sb.mtm
              span.price-total__key Total:
              span.price-total__number USD 430
            button.btn.btn-primary.btn-md.btn-block.mtm REGISTER NOW
</template>

<script>
import Tabs from '@/components/Tabs'
import Tab from '@/components/Tab'
import StarScore from '@/components/StarScore'
import 'slick-carousel/slick/slick.css'
import 'slick-carousel/slick/slick'

export default {
  components: {Tabs, Tab, StarScore},
  data() {
    return {
      activeTab: 'General Details',
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    $(this.$el).find('.crousel').slick({
      slidesToShow: 4,
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
@import "~@/assets/css/global.scss";
.Course{
  .container {
    width: 1400px;
    margin: 40px auto 140px auto;
  }
  .card2 {
    border-radius: 4px;
    box-shadow: 0px 3px 20.37px 0.63px rgba(159, 159, 159, 0.31);
  }
  .card2_right {
  }
  .card2__title {
    background: rgb(67,67,67);
    color: rgb(255,255,255);
    padding: 10px 0 10px 40px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    font-weight: bold;
  }
  .card2__body {
    padding: 20px 20px 20px 20px;
  }
  .card2_left-wrapper{
    width: 980px;
  }
  .card2_left{
    .card2__body {
      padding: 40px;
    }
    .title2{
      margin-top: 20px;
    }
  }
  .card2_right{
    width: 350px;
    .card2__title {
      padding-left: 16px;
      .icon{
        font-size: 16px;
        position: relative;
        top: -2px;
        margin-right: 8px;
      }
    }
  }
  .title2 {
    margin: 0 0 25px 0;
    font-weight: bold;
    font-size: 30px;
  }
  .instructors-info {
    width: 220px;
    flex-shrink: 0;
  }
  .title3{
    font-weight: bold;
  }
  .instructor-photo{
    width: 160px;
    height: 115px;
    border: 1px solid #ccc;
  }
  .instructor-footer{}
  .instructor-avatar{
    $side: 45px;
    width: $side;
    height: $side;
    border-radius: 100px;
    margin-right: -10px;
  }
  .instructor-number{
    margin-left: 30px;
    font-weight: bold;
    color: #888;
    vertical-align: middle;
  }
  .course-detail {
    flex-grow: 1;
    line-height: 25px;
    position: relative;
    .key {
      width: 120px;
      flex-shrink: 0;
      font-weight: bold;
    }
    .value {
      flex-grow: 0;
    }
    .google-map-icon{
      vertical-align: sub;
    }
    .meta {
      width: 95px;
      position: absolute;
      right: 0;
      top: 0;
    }
    .views {
      display: inline;
      font-size: 13px;
    }
    .collect{
      font-size: 18px;
      color: #aaa;
      cursor: pointer;
    }
    .collected{
      color: #e03e3e;
    }
    .share-btdivn{
      font-weight: bold;
      color: #fff;
      background: rgb(170, 170, 170);
      padding: 0px;
      text-transform: capitalize;
      .icon{
        font-size: 16px;
      }
      &:hover{
        background: $bg2;
      }
      &:active{
        background: darken($bg2, 20%);
      }
    }
  }
  // bottom
  .advertisement{
    a{
      width: 50%;
      display: inline-block;
    }
    img{
      width: 100%;
    }
  }
  // right
  .title2_sm {
    font-weight: bold;
    font-size: 21px;
  }
  .date-range {
    font-size: 16px;
    .icon{
      position: relative;
      top: -2px;
    }
  }
  .room {
    padding: 10px 10px 10px 10px;
    border: 2px solid #ccc;
    border-radius: 1px;
    .Checkbox{
      margin-top: 5px;
      margin-right: 5px;
    }
  }
  .room__info {

  }
  .room__price {
    padding: 5px 0 5px 0;
    font-weight: bold;
    font-size: 16px;
  }
  .room__oprice {
    font-size: 13px;
    .number{
      text-decoration: line-through;
    }
  }
  .room__type {
    font-size: 13px;
  }
  .room__early-bird {
    background: rgb(255,178,0);
    color: rgb(255,255,255);
    padding: 2px 7px;
    font-size: 12px;
    font-weight: bold;
    position: absolute;
    top: 10px;
    right: 0;
  }
  .additional {
    display: flex;
    align-items: center;
  }
  .additional__line {
    height: 2px;
    background: #bbb;
    flex-grow: 1;
  }
  .additional__text {
    font-weight: 300;
    font-size: 13px;
    margin-left: 10px;
    margin-right: 10px;
  }
  .price-line {
    border-bottom: 1px solid #ccc;
    padding: 5px 0;
  }
  .price-total {
    font-size: 21px;
    font-weight: bold;
  }
  .price-key {
    font-size: 13px;
  }
  .price-number {
    color: rgb(99, 202, 206);
    font-weight: bold;
  }
  .price-total__key {
  }
  .price-total__number {
    color: rgb(99, 202, 206);
  }

  // general-detail
  .general-detail {
    padding: 50px 0 50px 0;
  }
  .general-detail__paragraph {
    margin: 0 0 35px 0;
  }
  .general-detail__key {
    font-weight: bold;
    font-size: 18px;
  }
  .general-detail__value {
    margin: 10px 0 0 0;
  }
  .send-btn {
    .icon{
      font-size: 18px;
    }
  }
  // host-provider
  .host-provider {

  }
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
      width: 220px;
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
  .comment__date{
    margin-top: 10px;
    text-align: right;
    font-size: 13px;
  }
  // accomodation
  .accomodation {
    padding: 40px 0;
  }
  .accomodation-photos {

  }
  .accomodation-photo-wrapper {
    img{
      width: 220px;
    }
  }
  .accomodation-line {
    display: flex;
    padding: 25px 0;
    line-height: 25px;
    border-bottom: 1px solid #ddd;
  }
  .accomodation-key {
    width: 180px;
    margin-right: 20px;
  }
  .accomodation-value {

  }
  .accomodation-option{
    text-align: center;
    .icon{
      font-size: 38px;
    }
  }
}
</style>
