<template lang="pug">
.Home
  .big-banner
      AspectImage.big-banner-img(src="https://picsum.photos/1900/800?image=12" :aspect="2.5")
  .find-courses()
      el-select.country(v-model="findCourses.country" size="large" placeholder="Select Country")
      br.hidden-lg-and-up
      el-select.subject(v-model="findCourses.subject" size="large" placeholder="Select Subject")
      br.hidden-lg-and-up
      el-button(type="primary" size="large") Find Courses
  .home-block.most-viewed-block.hidden-sm-and-down
    .container
      h2.home-block-title  Most Viewed
      .cards
        //- 2nd
        CourseCard(
          title="English Max Course (18 hrs/week)"
          img="https://picsum.photos/400/300?image=50"
          :imgAspect="1.82"
        )
          img.number-mark(src="~assets/img/2nd.png")
          .text-area
            .info
              Icon(name="graduation-hat")
              span Connect English Language Institute- Mission Valley
            .info
              Icon(name="position")
              span SAN DIEGO, USA
            .info
              Icon(name="calendar")
              span 20th Feb - 30th March, 2017
            .info
              //- +icon('user')
              Icon(name="user")
              span 5 Spaces left
        //- 1st
        CourseCard(
          title="English Max Course (18 hrs/week)"
          img="https://picsum.photos/400/300?image=51"
          :imgAspect="1.82"
        )
          img.number-mark(src="~assets/img/1st.png")
          .text-area
            .info
              Icon(name="graduation-hat")
              span Connect English Language Institute- Mission Valley
            .info
              Icon(name="position")
              span SAN DIEGO, USA
            .info
              Icon(name="calendar")
              span 20th Feb - 30th March, 2017
            .info
              //- +icon('user')
              Icon(name="user")
              span 5 Spaces left
        //- 3rd
        CourseCard(
          title="English Max Course (18 hrs/week)"
          img="https://picsum.photos/400/300?image=52"
          :imgAspect="1.82"
        )
          img.number-mark(src="~assets/img/3rd.png")
          .text-area
            .info
              Icon(name="graduation-hat")
              span Connect English Language Institute- Mission Valley
            .info
              Icon(name="position")
              span SAN DIEGO, USA
            .info
              Icon(name="calendar")
              span 20th Feb - 30th March, 2017
            .info
              //- +icon('user')
              Icon(name="user")
              span 5 Spaces left
        //- .course-card
        //-   img.number-mark(src="~assets/img/2nd.png")
        //-   .course-card-title English Max Course (18 hrs/week)
        //-   a.img-area.has-read-more(href="#")
        //-     AspectImage(src="https://picsum.photos/400/300?image=50" :aspect="1.82")
        //-     .price USD 300,000
        //-     //- +readMore
        //-   .text-area
        //-     .col-left
        //-       .info
        //-         //- +icon('graduation-hat')
        //-         .text-area2 Connect English Language Institute- Mission Valley
        //-       .info
        //-         //- +icon('position')
        //-         .text-area2 SAN DIEGO, USA
        //-       .info
        //-         //- +icon('calendar')
        //-         .text-area2 20th Feb - 30th March, 2017
        //-     .col-right
        //-       .info
        //-         //- +icon('user')
        //-         .text-area2 5 Spaces left
        //- //- 1st
        //- .card
        //-   img.number-mark(src="~assets/img/1st.png")
        //-   .title English Max Course (18 hrs/week)
        //-   a.img-area.has-read-more(href="#")
        //-     img.img(v-lazy="'/static/pictures/most-viewed2.jpg'")
        //-     .price USD 300,000
        //-     +readMore
        //-   .text-area
        //-     .col-left
        //-       .info
        //-         +icon('graduation-hat')
        //-         .text-area2 Connect English Language Institute- Mission Valley
        //-       .info
        //-         +icon('position')
        //-         .text-area2 SAN DIEGO, USA
        //-       .info
        //-         +icon('calendar')
        //-         .text-area2 20th Feb - 30th March, 2017
        //-     .col-right
        //-       .info
        //-         +icon('user')
        //-         .text-area2 5 Spaces left
        //-     .clearfix
        //- //- 3rd
        //- .card
        //-   img.number-mark(v-lazy="~assets/img/3rd.png")
        //-   .title English Max Course (18 hrs/week)
        //-   a.img-area.has-read-more(href="#")
        //-     img.img(v-lazy="'/static/pictures/most-viewed3.jpg'")
        //-     .price USD 300,000
        //-     +readMore
        //-   .text-area
        //-     .col-left
        //-       .info
        //-         +icon('graduation-hat')
        //-         .text-area2 Connect English Language Institute- Mission Valley
        //-       .info
        //-         +icon('position')
        //-         .text-area2 SAN DIEGO, USA
        //-       .info
        //-         +icon('calendar')
        //-         .text-area2 20th Feb - 30th March, 2017
        //-     .col-right
        //-       .info
        //-         +icon('user')
        //-         .text-area2 5 Spaces left
        //-     .clearfix
  .home-block.featured-courses-block.bg-grey.hidden-sm-and-down
    .container
      h2.home-block-title  Featured Courses
      el-row(:gutter="16")
        el-col(:span="12")
          CourseCard(
            title="English Max Course (18 hrs/week)"
            img="https://picsum.photos/400/300?image=54"
            :imgAspect="1.82"
          )
            .text-area
              .info
                Icon(name="graduation-hat")
                span Connect English Language Institute- Mission Valley
              .info
                Icon(name="position")
                span SAN DIEGO, USA
              .info
                Icon(name="calendar")
                span 20th Feb - 30th March, 2017
              .info
                //- +icon('user')
                Icon(name="user")
                span 5 Spaces left
        el-col(:span="12")
          CourseCard(
            title="English Max Course (18 hrs/week)"
            img="https://picsum.photos/400/300?image=55"
            :imgAspect="1.82"
          )
            .text-area
              .info
                Icon(name="graduation-hat")
                span Connect English Language Institute- Mission Valley
              .info
                Icon(name="position")
                span SAN DIEGO, USA
              .info
                Icon(name="calendar")
                span 20th Feb - 30th March, 2017
              .info
                //- +icon('user')
                Icon(name="user")
                span 5 Spaces left
        el-col
          br
        el-col(:span="8" v-for="i in 3" :key="i")
          CourseCard(
            title="English Max Course (18 hrs/week)"
            img="https://picsum.photos/400/300?image=56"
            :imgAspect="1.82"
          )
            .text-area
              .info
                Icon(name="graduation-hat")
                span Connect English Language Institute- Mission Valley
              .info
                Icon(name="position")
                span SAN DIEGO, USA
              .info
                Icon(name="calendar")
                span 20th Feb - 30th March, 2017
              .info
                //- +icon('user')
                Icon(name="user")
                span 5 Spaces left
  .home-block.early-bird-block
    .container
      el-row.mtm.mbxl.hidden-md-and-down(:gutter="16")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'https://picsum.photos/600/250?image=57'")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'https://picsum.photos/600/250?image=58'")
      .home-block-title-bar
        .home-block-title.home-block-title--left Early Bird Courses
        a.view-more(href="#") View more »
      el-row(:gutter="16" v-if="!mini")
        el-col.mbm(:span="8" v-for="i in 6" :key="i")
          CourseCard(
            title="English Max Course (18 hrs/week)"
            img="https://picsum.photos/400/300?image=59"
            :imgAspect="1.82"
            mark="Early Bird SALE"
            price="USD 300,000"
            originalPrice="USD 600,000"
          )
            .text-area
              .info
                Icon(name="graduation-hat")
                span Connect English Language Institute- Mission Valley
              .info
                Icon(name="position")
                span SAN DIEGO, USA
              .info
                Icon(name="calendar")
                span 20th Feb - 30th March, 2017
              .info
                //- +icon('user')
                Icon(name="user")
                span 5 Spaces left
      Carousel2(v-else)
        CourseCard(
          v-for="i in 6" :key="i + 'str'"
          title="English Max Course (18 hrs/week)"
          img="https://picsum.photos/400/300?image=59"
          :imgAspect="1.82"
          mark="Early Bird SALE"
          price="USD 300,000"
          originalPrice="USD 600,000"
        )
          .text-area
            .info
              Icon(name="graduation-hat")
              span Connect English Language Institute- Mission Valley
            .info
              Icon(name="position")
              span SAN DIEGO, USA
            .info
              Icon(name="calendar")
              span 20th Feb - 30th March, 2017
            .info
              //- +icon('user')
              Icon(name="user")
              span 5 Spaces left
        .carousel-item(v-for="i in 10" :key="i")
  .home-block.soon-start-block.bg-grey
    .container
      .home-block-title-bar
        .home-block-title.home-block-title--left Soon to Start Courses
        a.view-more(href="#") View more »
      el-row(:gutter="16" v-if="!mini")
        el-col.mbm(:span="8" v-for="i in 6" :key="i")
          CourseCard(
            title="English Max Course (18 hrs/week)"
            img="https://picsum.photos/400/300?image=59"
            :imgAspect="1.82"
            price="USD 300,000"
          )
            .text-area
              .info
                Icon(name="graduation-hat")
                span Connect English Language Institute- Mission Valley
              .info
                Icon(name="position")
                span SAN DIEGO, USA
              .info
                Icon(name="calendar")
                span 20th Feb - 30th March, 2017
              .info
                //- +icon('user')
                Icon(name="user")
                span 5 Spaces left
      Carousel2(v-else)
        CourseCard(
          v-for="i in 6" :key="i + 'str'"
          title="English Max Course (18 hrs/week)"
          img="https://picsum.photos/400/300?image=59"
          :imgAspect="1.82"
          price="USD 300,000"
        )
          .text-area
            .info
              Icon(name="graduation-hat")
              span Connect English Language Institute- Mission Valley
            .info
              Icon(name="position")
              span SAN DIEGO, USA
            .info
              Icon(name="calendar")
              span 20th Feb - 30th March, 2017
            .info
              //- +icon('user')
              Icon(name="user")
              span 5 Spaces left
  .home-block.big-block
    .container
      el-row.mtm.mbxl.hidden-md-and-down(:gutter="16")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'https://picsum.photos/600/250?image=57'")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'https://picsum.photos/600/250?image=58'")
      .home-block-title Adventures
      Carousel2.mtm
        .carousel-item(v-for="i in 10" :key="i")
          a.img-area(href="#")
            HasReadMore
              AspectImage(:src="'https://picsum.photos/200/140?image=6'+i" :aspect="1.43")
          .text-area Business
      .home-block-title.mtl Lifestyle
      Carousel2.mtm
        .carousel-item(v-for="i in 10" :key="i")
          a.img-area(href="#")
            HasReadMore
              AspectImage(:src="'https://picsum.photos/200/140?image=6'+i" :aspect="1.43")
          .text-area Business
      //-
      .home-block-title.mtl Categories
      Carousel2.mtm
        .carousel-item(v-for="i in 10" :key="i")
          a.img-area(href="#")
            HasReadMore
              AspectImage(:src="'https://picsum.photos/200/140?image=6'+i" :aspect="1.43")
          .text-area Business
      //-
      .home-block-title.mtl Countries
      Carousel2.mtm(:responsive="[2,3,4,5]")
        .carousel-item(v-for="i in 10" :key="i")
          a.img-area(href="#")
            HasReadMore
              AspectImage(:src="'https://picsum.photos/200/300?image=6'+i" :aspect="0.66")
          .text-area London
  .home-block.subscribe-block(v-lazy:background="subscribeBackground")
    .container
      .title Subscribe to our mailing list
      .title2 BE THE FIRST TO GET LATEST NEWS AND OFFERS!
      form.mtl
        el-row(:gutter="16")
          el-col.mbm(:span="16" :xs="24")
            el-input.input(placeholder="Enter your email")
          el-col(:span="8" :xs="24")
            el-button.btn() Subscribe!
</template>

<script>
import CourseCard from '@/components/CourseCard.vue'
import Carousel2 from '@/components/Carousel2'
import subscribeBackground from '@/assets/img/subscribe-background.jpg'

const mixins = []
if (process.browser) {
  mixins.push(require('@/components/windowSize').default)
}
export default {
  layout: 'nomenu',
  components: {CourseCard, Carousel2},
  mixins,
  data() {
    return {
      findCourses: {
        country: null,
        subject: null,
      },
      subscribeBackground,
    }
  },
  computed: {
    mini() {
      return process.browser && this.window.innerWidth < 768
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.big-banner-img{
  min-height: 300px;
}
.find-courses{
  background-color: #f3f2f0;
  padding-top: 25px;
  padding-bottom: 30px;
  text-align: center;
  $w: 330px;
  .country{
    width: $w;
    display: inline-block;
  }
  .subject{
    width: $w;
    display: inline-block;
    margin-left: 25px;
  }
  .el-button{
    width: 210px;
    margin-left: 100px;
  }
  @media(max-width: $large){
    .subject{
      margin: 25px 0;
    }
    .el-button{
      width: $w - 2px;
      margin-left: 0;
    }
  }
}
// common
.home-block {
  padding-top: 60px;
  padding-bottom: 80px;
}

.home-block-title {
  font-size: 60px;
  font-weight: lighter;
  text-align: center;
  margin-bottom: 50px;
  // xs extra small 特小屏幕 手机
  @media(max-width: $small) {
    font-size: 25px;
  }
}
.home-block-title--left{
  text-align: left;
}

.home-block {
  .course-card-title {
    padding-left: 10px;
  }
  .text-area {
    .icon{
      color: $primaryColor;
    }
  }
}
.home-block-title-bar{
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items:baseline;
  margin-bottom: 20px;
  .home-block-title{
    margin: 0;
  }
}
.view-more{
  // position: absolute;
  // right: 0;
  // bottom: 8px;
  font-size: 21px;
  font-weight: 500;
  color: #ffb200;
  text-transform: uppercase;
  // xs extra small 特小屏幕 手机
  @media(max-width: $small) {
    font-size: 16px;
  }
}

.carousel-item{
  .text-area {
    font-size: 16px;
    font-weight: 500;
    text-align: center;
    margin-top: 20px;
  }
}
.carousel-btn{
  position: relative;
  top: -15px;
}
//
.Home .course-card .text-area .icon-graduation-hat{
  // this icon too big
  font-size: 16px;
}
.most-viewed-block{
  .cards{
    position: relative;
  }
  $width: 38%;
  .course-card {
    width: $width;
    position: relative;
  }
  .course-card-title {
    padding-left: 45px;
  }
  .number-mark {
    position: absolute;
    left: -25px;
    top: -5px;
    background-color: transparent;
    width: 64px;
    height: 64px;
    z-index: 2;
  }
  $scale: 0.76;
  $offset: ($width - $width * $scale) / 2;

  .course-card:nth-child(1) {
    position: absolute;
    left: -$offset;
    transform: scale($scale);
  }

  .course-card:nth-child(3) {
    position: absolute;
    right: -$offset;
    top: 0;
    transform: scale($scale);
  }
  // center card
  .course-card:nth-child(2) {
    margin: 0 auto;
  }
}
.soon-start-block{
  $color: #7cc576;
  .view-more{
    color: $color;
  }
  .text-area{
    .icon{
      color: $color;
    }
  }
}
.big-block{
  .home-block-title{
    font-size: 50px;
  }
}

.subscribe-block {
  text-align: center;
  color: rgb(255, 255, 255);
  background-size: cover;
  .title {
    font-size: 60px;
    font-weight: 300;
  }

  .title2 {
    margin-top: 15px;
    font-size: 21px;
    font-weight: 300;
    text-transform: uppercase;
  }
  form{
    width: 80%;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }
  input, button {
    // form control
    $height: 70px;
    height: $height;
    font-size: 21px;
    padding: 0 25px;
  }
  button {
    width: 100%;
    background-color: rgb(38, 38, 38);
    border: none;
    font-weight: 500;
    color: #fff;
  }
  @media(max-width: $medium){
    .title {
      font-size: 40px;
      font-weight: 300;
    }
  }
}
</style>
