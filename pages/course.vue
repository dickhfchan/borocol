<template lang="pug">
.course-page.container
  .space
  .space
  .space
  el-breadcrumb(separator='/')
    el-breadcrumb-item(:to="{name: 'index'}") Home
    el-breadcrumb-item Search Result
  .space
  .space
  Row(:gutter="[60, 20]")
    Col.card2_left-wrapper(:width="500")
      .card2.card2_left
        .card2__title Tony Vega class
        .card2__body
          .title2 5 Days Yoga Retreat in a luxury 5 Stars Resort, Okinawa
          .flex
            .instructors-info
              .title3.mbm Your Instructor / Host
              img.instructor-photo.mbl(src="https://picsum.photos/160/115?image=400")
              .instructor-footer
                .avatars
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=401")
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=402")
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=403")
                  img.instructor-avatar(src="https://picsum.photos/40/40?image=404")
                span.instructor-number
                  Icon(name="plus")
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
                Icon.collect.collected.mlm(name="heart" title="Collect / Uncollect")
                el-button.share-btn.btn-block.mts(type="primary")
                  Icon.mrs(name="share")
                  span Share
          .space
          .space
          el-tabs(v-model="activeTab")
            el-tab-pane(label="General Details" name="0")
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
                  el-button.send-btn(type="primary")
                    Icon(name="dialog")
                    span.mls Send Inquiry
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
            el-tab-pane(label="About Your Host / Provider" name="1")
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
                  .space
                  .space
                  .space
                  Carousel3(v-if="activeTab==='1'" :responsive="[2,3,3,4]")
                    .carousel-item(v-for="i in 10" :key="i")
                      AspectImage(:src="'https://picsum.photos/250/180?image=6'+i" :aspect="1.5")
                .reviews-total 281 Reviews (Based on Courses)
                form.comment-form.comment
                  .comment__left
                    img.comment__avatar(src="https://picsum.photos/150/150?image=415")
                    .comment__user-name Terry
                  .comment__right
                    .comment__name English Max Course
                    .mtm Rate your course
                      el-rate.mlm
                    .comment__content
                      el-input(type="textarea" :rows="5" placeholder="Share your experience")
                      .mtm
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
                      .comment__date May 30‘ 17
                  el-pagination.pull-right(:total="50" :page-size="10")
                  .clearfix
            el-tab-pane(label="Accomodation" name="2")
              .accomodation2
                Carousel3(v-if="activeTab==='2'" :responsive="[2,3,3,4]")
                  .carousel-item(v-for="i in 10" :key="i")
                    AspectImage(:src="'https://picsum.photos/250/180?image=6'+i" :aspect="1.5")
                .accomodation2-line.mtl
                  .accomodation2-key Options
                  .accomodation2-value
                    .accomodation2-option
                      Icon(name="house")
                      .mts Dorm
                .accomodation2-line
                  .accomodation2-key About the location:
                  .accomodation2-value Lorem \psum ‘5 swmp‘y dummy text or’ the prmtmg and typesemng \ndustry
                    br
                    | Lorem \psum has been the mdustry‘s standard dummy text ever smce the
                .accomodation2-line
                  .accomodation2-key Facilities:
                  .accomodation2-value Wm / mtchen / Swwmmmg poo‘ / Washmg machme/ gym / ba‘cony
                    br
                    | Othevs warary‘ garden
      .advertisement.flex.mtl
        a(href="javascript:void(0)")
          img(src="https://picsum.photos/500/220?image=405")
        a(href="javascript:void(0)")
          img(src="https://picsum.photos/500/220?image=406")
      .related-title.mtl You might be interested in
      el-row(:gutter="16").related.mtl
        el-col(:sm="12")
          .course-card2
            .course-card2__img-area(href="#")
              AspectImage(src="https://picsum.photos/500/300?image=401" :aspect="1.7")
              .mark Early Bird Sale
              .course-card2__collect.collected
                Icon(name="heart")
              .course-card2__meta.flex.justify-sb.align-c
                .flex.align-c
                  div
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=401")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=402")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=403")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=404")
                  span.instructor-more
                    Icon(name="plus")
                    | More
                span 1000 Views
            .course-card2__text-area
              .course-card2__title English Max Course
              .course-card2__address.mtm SAN D‘EGO, USA
              .flex.justify-sb.mts
                .course-card2__date Feb 20,16 , Mar 30,17
                .course-card2__price USD 600,000
        el-col(:sm="12")
          .course-card2
            .course-card2__img-area(href="#")
              AspectImage(src="https://picsum.photos/500/300?image=403" :aspect="1.7")
              .mark Early Bird Sale
              .course-card2__collect
                Icon(name="heart-o")
              .course-card2__meta.flex.justify-sb.align-c
                .flex.align-c
                  div
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=401")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=402")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=403")
                    img.instructor-avatar(src="https://picsum.photos/40/40?image=404")
                  span.instructor-more
                    Icon(name="plus")
                    | More
                span 1000 Views
            .course-card2__text-area
              .course-card2__title English Max Course
              .course-card2__address.mtm SAN D‘EGO, USA
              .flex.justify-sb.mts
                .course-card2__date Feb 20,16 , Mar 30,17
                .course-card2__price USD 600,000
    Col(:width="350")
      .card2_right.card2
        .card2__title
          Icon(name="user")
          | 5 SPACES LEFT
        .card2__body
          .title2_sm English Max Course
          .date-range.mtm
            Icon(name="calendar")
            |  Dec 20, 16 - Mar 30,17
          .room.flex.relative.mtm
            el-checkbox
            .room__info
              .room__price USD 2,000
              .room__oprice
                | Orignal
                span.number USD 2,300
              .room__type Single Room
            .room__early-bird EARLY BIRD
          .room.flex.relative.mts
            el-checkbox
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
              el-checkbox
              span.mls Down Payment
            QuestionCircle
          .price-line.flex.justify-sb.mtm
            span.price-key Program Fee
            span.price-number USD 1,800
          .price-line.flex.justify-sb
            span.price-key  Down Payment
            span.price-number USD 480
          .price-total.flex.justify-sb.mtm
            span.price-total__key Total:
            span.price-total__number USD 430
          .mtm
          el-button.btn-block.register-btn(type="primary" size="large") REGISTER NOW
</template>

<script>
import Carousel3 from '@/components/Carousel3'
export default {
  components: {Carousel3},
  data() {
    return {
      activeTab: '0',
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {},
  beforeDestroy() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
@import "~assets/style/course-card2.scss";
.course-page{
  .justify-sb {
    justify-content: space-between;
  }

  .justify-c {
    justify-content: center;
  }
  .align-c{
    align-items: center;
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
  .card2_left{
    .card2__body {
      padding: 40px;
    }
    .title2{
      margin-top: 20px;
    }
  }
  .card2_right{
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
  .instructor-footer{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
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
    .share-btn{
      padding: 8px;
      .icon{
        font-size: 14px;
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
    .el-checkbox{
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
  .accomodation2 {
    padding: 40px 0;
  }
  .accomodation2-photos {

  }
  .accomodation2-photo-wrapper {
  }
  .accomodation2-line {
    display: flex;
    padding: 25px 0;
    line-height: 25px;
    border-bottom: 1px solid #ddd;
  }
  .accomodation2-key {
    width: 180px;
    margin-right: 20px;
  }
  .accomodation2-value {

  }
  .accomodation2-option{
    text-align: center;
    .icon{
      font-size: 38px;
    }
  }
  .related-title {
      font-size: 18px;
      font-weight: 500;
      text-align: center;
  }
  .register-btn{
    padding-top: 15px;
    padding-bottom: 15px;
  }
}
</style>
