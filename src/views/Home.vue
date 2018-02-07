<template lang="pug">
include ../common.pug
mixin carouselItem(src, title)
  div
    .carousel-item
      a.img-area.has-read-more(href="#")
        img.img(v-lazy=`'${src}'`)
        +readMore
      .text-area= title
.Home
  .banner-bar(v-lazy:background-image="'/static/pictures/header.jpg'")
    .lb1
      .container
        .course-search-card.bg1.pull-right.hidden-xs.hidden-sm.hidden-md
          form.search-wrapper
            input.input(type="text" placeholder="Course Name...")
            button.btn-icon.no-bb
              +icon('arrow-right')
          .data-rows-wrapper
            .data-rows
              .data-row(v-for="i in 10")
                .img-area
                  img(v-lazy="'/static/pictures/header-course.jpg'")
                .text-area
                  .title English Max Course
                  .description
                    | Connect English Language Institute
                    br
                    | Mission Valley
                  .info SAN DIEGO, USA
  form.filter-bar.bg1
    .container
      select.select1.country-select(placeholder="Select Country")
        option Select Country
        option USA
      select.select1.subject-select(placeholder="Select Subject")
        option Select Subject
        option USA
      button.btn1 Find Courses
  .most-viewed-block.home-block.hidden-xs.hidden-sm
    .container
      h2.home-block-title  Most Viewed
      .cards
        //- 2nd
        .card
          img.number-mark(v-lazy="'/static/images/2nd.png'")
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/most-viewed1.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .col-left
              .info
                +icon('graduation-hat')
                .text-area2 Connect English Language Institute- Mission Valley
              .info
                +icon('position')
                .text-area2 SAN DIEGO, USA
              .info
                +icon('calendar')
                .text-area2 20th Feb - 30th March, 2017
            .col-right
              .info
                +icon('user')
                .text-area2 5 Spaces left
            .clearfix
        //- 1st
        .card
          img.number-mark(v-lazy="'/static/images/1st.png'")
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/most-viewed2.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .col-left
              .info
                +icon('graduation-hat')
                .text-area2 Connect English Language Institute- Mission Valley
              .info
                +icon('position')
                .text-area2 SAN DIEGO, USA
              .info
                +icon('calendar')
                .text-area2 20th Feb - 30th March, 2017
            .col-right
              .info
                +icon('user')
                .text-area2 5 Spaces left
            .clearfix
        //- 3rd
        .card
          img.number-mark(v-lazy="'/static/images/3rd.png'")
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/most-viewed3.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .col-left
              .info
                +icon('graduation-hat')
                .text-area2 Connect English Language Institute- Mission Valley
              .info
                +icon('position')
                .text-area2 SAN DIEGO, USA
              .info
                +icon('calendar')
                .text-area2 20th Feb - 30th March, 2017
            .col-right
              .info
                +icon('user')
                .text-area2 5 Spaces left
            .clearfix
  .featured-courses-block.home-block.bg1.hidden-xs.hidden-sm
    .container
      h2.home-block-title  Featured Courses
      .cards-bg
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-110055.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .col-left
              .info
                +icon('graduation-hat')
                .text-area2 Connect English Language Institute- Mission Valley
              .info
                +icon('position')
                .text-area2 SAN DIEGO, USA
              .info
                +icon('calendar')
                .text-area2 20th Feb - 30th March, 2017
            .col-right
              .info
                +icon('user')
                .text-area2 5 Spaces left
            .clearfix
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-111253.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .col-left
              .info
                +icon('graduation-hat')
                .text-area2 Connect English Language Institute- Mission Valley
              .info
                +icon('position')
                .text-area2 SAN DIEGO, USA
              .info
                +icon('calendar')
                .text-area2 20th Feb - 30th March, 2017
            .col-right
              .info
                +icon('user')
                .text-area2 5 Spaces left
            .clearfix
      .cards-sm
        //- 3
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/Layer13copy.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //- 4
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-54276copy.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //- 5
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/gerlitz-glacier-mountains-in-the-morning-paragliding-65677copy.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
  .early-bird-courses-block.home-block
    .container
      el-row.mtm.mbxl.hidden-xs.hidden-sm.hidden-md(:gutter="15")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'/static/pictures/Layer103.jpg'")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'/static/pictures/Layer102.jpg'")
      .title-bar
        .home-block-title.title Early Bird Courses
        a.more(href="#") View more »
      //-
      .cards
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/Layer13copy.jpg'")
            .mark Early Bird SALE
            .price
              span USD 300,000
              .original-price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-54276copy.jpg'")
            .mark Early Bird SALE
            .price
              span USD 300,000
              .original-price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-29737.jpg'")
            .mark Early Bird SALE
            .price
              span USD 300,000
              .original-price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/Layer13copy.jpg'")
            .mark Early Bird SALE
            .price
              span USD 300,000
              .original-price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-54276copy.jpg'")
            .mark Early Bird SALE
            .price
              span USD 300,000
              .original-price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-29737.jpg'")
            .mark Early Bird SALE
            .price
              span USD 300,000
              .original-price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
  .soon-to-start-courses-block.home-block.bg1
    .container
      .title-bar
        .home-block-title.title Soon to Start Courses
        a.more(href="#") View more »
      .cards
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/hands-people-woman-working.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/hands-people-woman-working.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-251225.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/hands-people-woman-working.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/hands-people-woman-working.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
        //-
        .card
          .title English Max Course (18 hrs/week)
          a.img-area.has-read-more(href="#")
            img.img(v-lazy="'/static/pictures/pexels-photo-251225.jpg'")
            .price USD 300,000
            +readMore
          .text-area
            .info
              +icon('graduation-hat')
              .text-area2 Connect English Language Institute- Mission Valley
            .info
              +icon('position')
              .text-area2 SAN DIEGO, USA
            .info
              +icon('calendar')
              .text-area2 20th Feb - 30th March, 2017
            .info
              +icon('user')
              .text-area2 5 Spaces left
  .big-block.home-block
    .container
      el-row.mtm.hidden-xs.hidden-sm.hidden-md(:gutter="15")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'/static/pictures/Layer103.jpg'")
        el-col(:span="12")
          a.display-b
            img.w-100(v-lazy="'/static/pictures/Layer102.jpg'")
      .home-block-title Adventures
      .carousel._1.mtm
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Specially')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Professional')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Professional')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Professional')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Business')
      .home-block-title Lifestyle
      .carousel._1.mtm
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Specially')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Professional')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Professional')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Business')
      //-
      .home-block-title Categories
      .carousel._1.mtm
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Specially')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Professional')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Professional')
        +carouselItem('/static/pictures/pexels-photo-110469copy.jpg', 'Business')
        +carouselItem('/static/pictures/Layer15copy.jpg', 'Business')
      //-
      .home-block-title Countries
      .carousel._2
        +carouselItem('/static/pictures/Layer7.jpg', 'London')
        +carouselItem('/static/pictures/Layer8.jpg', 'Paris')
        +carouselItem('/static/pictures/Layer9.jpg', 'Tokyo')
        +carouselItem('/static/pictures/Layer10.jpg', 'Havana')
        +carouselItem('/static/pictures/Layer11.jpg', 'Cape Town')
        +carouselItem('/static/pictures/Layer10.jpg', 'Miami')
        +carouselItem('/static/pictures/Layer10.jpg', 'Havana')
        +carouselItem('/static/pictures/Layer11.jpg', 'Cape Town')
        +carouselItem('/static/pictures/Layer10.jpg', 'Miami')
  .subscribe-block.home-block
    img.back-img.hidden-xs(v-lazy="'/static/images/subscribe-background.jpg'")
    .title Subscribe to our mailing list
    .title2 BE THE FIRST TO GET LATEST NEWS AND OFFERS!
    form
      //- fc is form control
      input.input._fc(type="text" placeholder="Enter your email")
      button.btn._fc() Subscribe!
</template>

<script>
import routes from '@/routes/index'
import {timeoutPromise} from '@/utils'
import windowSize from '@/components/windowSize'
import mounted from '@/components/mounted'
import {waitFor} from 'helper-js'
import 'slick-carousel'
import 'slick-carousel/slick/slick.css'

export default {
  mixins: [windowSize, mounted],
  components: {},
  data() {
    return {
      routes: routes,
    }
  },
  computed: {
    mini() { return this.window.innerWidth <= 768 },
  },
  watch: {
    'window.innerWidth': {
      immediate: true,
      async handler(value) {
        await this.mounted
        setTimeout(() => {
          this.updateCarouselItemWidth()
        }, 100);
      }
    },
    mini: {
      immediate: true,
      async handler(mini, old) {
        if (old === mini) {
          return
        }
        await this.mounted
        const wrapperHtmlStr = '<div class="card-wrapper-to-keep-shadow-in-slick"></div>'
        const cards = $('.soon-to-start-courses-block .cards, .early-bird-courses-block .cards')
        const carousels = $('.big-block .carousel')
        if (mini) {
          cards.add(carousels).addClass('mini')
          cards.find('.card').wrap(wrapperHtmlStr)
          cards.slick({
            dots: true,
            arrows: false,
            autoplay: true,
          })
          // carousels
          const last = carousels.last()
          if (carousels.hasClass('slick-slider')) {
            carousels.slick('unslick')
            await waitFor(() => !carousels.hasClass('.slick-slider'), 50)
          }
          carousels.not(last).slick({
            dots: true,
            arrows: false,
            autoplay: true,
          })
          last.slick({
            dots: true,
            arrows: false,
            autoplay: true,
            slidesToShow: 2,
            slidesToScroll: 2,
          })
        } else {
          if (cards.hasClass('mini')) {
            cards.add(carousels).removeClass('mini').slick('unslick')
            cards.find('.card').unwrap()
          }
          $('.carousel').slick({
            infinite: false,
            slidesToShow: 5,
            slidesToScroll: 1,
            prevArrow: '<div class="carousel-btn left-btn"><span class="icon icon-left-open-big"></span></div>',
            nextArrow: '<div class="carousel-btn right-btn"><span class="icon icon-right-open-big"></span></div>',
            responsive: [
              {
                breakpoint: this.$state.style.large,
                settings: {
                  slidesToShow: 4,
                  slidesToScroll: 1,
                }
              },
              {
                breakpoint: this.$state.style.medium,
                settings: {
                  slidesToShow: 3,
                  slidesToScroll: 1,
                }
              },
            ]
          })
          setTimeout(() => {
            this.updateCarouselItemWidth()
          }, 100);
        }
      },
    }
  },
  methods: {
    updateCarouselItemWidth() {
      $('.slick-slider').each((i, el) => {
        el = $(el)
        const list = el.find('.slick-list')
        const items = el.find('.carousel-item')
        const space = 20
        const n = Math.round(list.width() / el.find('.slick-slide:eq(0)').width())
        const w = (list.width() - (n - 1) * space) / n
        items.width(w)
      })
    },
  },
  // created() {},
  mounted() {
  },
  beforeDestroy() {
    try {
      $('.slick-slider').slick('unslick');
    } catch (e) {}
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Home{
  // common

  .carousel {
    position: relative;

    .carousel-btn {
      color: #7D7D7D;
      cursor: pointer;
      position: absolute;
      font-size: 40px;
    }

    .left-btn {
      right: 101%;
      right: calc(100% + 25px);
    }

    .right-btn {
      left: 101%;
      left: calc(100% + 25px);
    }
  }

  .carousel-item{
    width: 260px;
    img{
      width: 100%;
    }
    .text-area {
      font-size: 16px;
      font-weight: 500;
      text-align: center;
      margin-top: 20px;
    }
  }
  //
  .banner-bar {
    height: 770px;
    overflow: hidden;
    background-position: center;
    background-size: cover;

    .banner {
      // width: 100%;
    }
    position: relative;
    // layout block
    .lb1 {
      // position: absolute;
      // top: 0;
      // width: 100%;
      overflow: visible;
    }
  }

  .course-search-card {
    $scale: 1;
    $width: 480px * $scale;
    $height: $width * 1.3;
    $cardHeight: $height;
    width: $width;
    height: $height;
    padding: 40px 30px 40px 40px;

    .search-wrapper {
      $height: 40px;
      height: $height;
      border-bottom: 3px solid #fff;
      position: relative;
      //
      $iconH: 30px;

      .btn-icon {
        @include noFocusOutline;
        width: $iconH;
        height: $iconH;
        line-height: $iconH;
        text-align: center;
        position: absolute;
        top: 0;
        right: 0;

        .icon {
          font-size: 25px;
          color: #cecece;
        }
      }

      .input {
        @include noFocusOutline;
        @include noBb;
        width: 100%;
        height: 100%;
        font-size: 18px;
        padding-right: $iconH;
      }
    }

    .data-rows-wrapper {
      margin-top: 30px;
      height: $cardHeight - 40 * 2 - 30 - 40;
      overflow-y: auto;
    }

    .data-row {
      height: 70px;
      margin-bottom: 20px;
      $imgAreaWidth: 100px;

      .img-area {
        width: $imgAreaWidth;
        height: 100%;
        float: left;

        img {
          width: 100%;
          height: 100%;
        }
      }

      .text-area {
        margin-left: $imgAreaWidth + 15px;

        .title {
          font-size: 13px;
          font-weight: bold;
          color: #444444;
        }

        .description {
          font-size: 11px;
          color: #888888;
          line-height: 15px;
          margin-bottom: 6px;
        }

        .info {
          font-size: 11px;
          color: #888888;
        }
      }
    }
    // lg large to superLarge
    @media(min-width: $large) and (max-width: $superLarge) {
      $scale: 0.7;
      $width: 480px * $scale;
      $height: $width * 1.5;
      $cardHeight: $height;
      width: $width;
      height: $height;

      .data-rows-wrapper {
        height: $cardHeight - 40 * 2 - 30 - 40;
      }
    }
  }

  .filter-bar {
    padding-top: 25px;
    padding-bottom: 30px;
    text-align: center;

    .select1 {
      width: 330px;
    }

    .country-select {}

    .subject-select {
      margin-left: 25px;
    }

    .btn1 {
      width: 210px;
      margin-left: 100px;
      font-size: 17px;
      font-weight: bold;
    }
    // md
    .container {
      // md medium 中等屏幕 桌面显示器
      @media(max-width: $large) and (min-width: $medium) {
        display: flex;
        justify-content: space-between;
      }
      // xs sm
      @media(max-width: $medium) {
        display: block;
        .select1, .btn1{
          display: block;
          width: 350px;
          max-width: 90%;
          margin: 0 auto;
        }
        .select1{
          margin-bottom: 15px;
        }
      }
    }
  }

  // header, banner, filter form end
  .home-block {
    padding-top: 60px;
    padding-bottom: 80px;
  }

  .home-block-title {
    font-size: 60px;
    font-weight: lighter;
    text-align: center;
    margin: 0;
    // xs extra small 特小屏幕 手机
    @media(max-width: $small) {
      font-size: 30px;
    }
  }

  .home-block {
    .card {
      position: relative;

      .number-mark {
        position: absolute;
        left: -23px;
        top: -5px;
        background-color: transparent;
        width: 64px;
        height: 64px;
        z-index: 2;
      }

      .mark {
        background-color: rgb(255, 178, 0);
        position: absolute;
        left: 0;
        top: 10%;
        color: #fff;
        font-weight: bold;
        padding: 5px 10px;
      }

      .title {
        padding-left: 30px;
      }

      .img-area {
        .price {
          background-color: rgb(112, 112, 112);
          position: absolute;
          top: 70%;
          right: 0;
          padding: 5px 10px;
          font-size: 16px;
          color: rgb(255, 255, 255);
          font-weight: bold;
        }

        .original-price {
          font-size: 13px;
          text-align: right;
          text-decoration: line-through;
        }
      }

      .text-area {
        .col-left {
          width: 80%;
          float: left;
        }

        .col-right {
          width: 20%;
          float: right;

          .info {
            font-size: 10px;
          }
        }
      }
    }
    @media(max-width: $superLarge) {
      .card {
        .text-area {
          .col-left {
            float: none;
            width: 100%;
          }

          .col-right {
            float: none;
            width: 100%;
          }
        }
      }
    }
    // xs extra small 特小屏幕 手机
    @media(max-width: $small) {
      .mini{
        .card-wrapper-to-keep-shadow-in-slick{
          padding: 0 10px;
          padding-bottom: 15px;
        }
        .card{
          width: auto;
        }
      }
    }
  }
  $iconTealColor: #47CBCD;

  .most-viewed-block {
    .cards {
      margin-top: 50px;
      position: relative;
    }
    $width: 38%;

    .card {
      width: $width;

      .title {
        padding-left: 40px;
      }
    }
    $scale: 0.76;
    $offset: ($width - $width * $scale) / 2;

    .card:nth-child(1) {
      position: absolute;
      left: -$offset;
      transform: scale($scale);
    }

    .card:nth-child(3) {
      position: absolute;
      right: -$offset;
      top: 0;
      transform: scale($scale);
    }
    // center card
    .card:nth-child(2) {
      margin: 0 auto;
    }

    .img-area {
      height: 0;
      padding-bottom: 55%;
    }

    .text-area {
      .icon {
        color: $iconTealColor;
      }
    }
  }

  .featured-courses-block {
    .cards-bg {
      margin-top: 40px;
      display: flex;
      justify-content: space-between;

      .card {
        width: 49.5%;
      }

      .img-area {
        height: 0;
        padding-bottom: 54%;
      }
    }

    .cards-sm {
      margin-top: 30px;
      display: flex;
      justify-content: space-between;

      .card {
        width: 32.7%;
      }

      .img-area {
        height: 0;
        padding-bottom: 54%;
      }
    }

    .text-area {
      .icon {
        color: $iconTealColor;
      }
    }
  }

  .early-bird-courses-block,
  .soon-to-start-courses-block {
    $iconColor: rgb(255, 178, 0);

    .title-bar {
      position: relative;

      .title {
        text-align: left;
      }

      .more {
        position: absolute;
        right: 0;
        bottom: 8px;
        font-size: 21px;
        font-weight: 500;
        color: $iconColor;
        text-transform: uppercase;
      }
    }
    $space: 3%;

    .cards {
      margin-top: 40px;
      margin-bottom: -$space;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
    }

    .card {
      width: 32%;
      margin-bottom: $space;

      .img-area {
        height: 0;
        padding-bottom: 55.3%;
      }

      .text-area {
        .icon {
          color: $iconColor;
        }
      }
    }
    @media(max-width: $large) {
      .card {
        width: 49%;
      }
    }
    @media(max-width: $medium) {
      .title-bar {
        .more {
          position: static;
        }
      }
    }

    .cards.mini {
      display: block;

      .slick-list {
        margin-bottom: 20px;
      }

      .card {
        margin-bottom: 0;
      }
    }
  }

  .soon-to-start-courses-block {
    $iconColor: #7CC576;

    .title-bar {
      .more {
        color: $iconColor;
      }
    }

    .card {
      .text-area {
        .icon {
          color: $iconColor;
        }
      }
    }
  }
  .big-block {

    .home-block-title {
      font-size: 50px;
      margin-top: 70px;
    }

    .carousel._1 {
      .carousel-btn {
        top: 36px;
      }

      .carousel-item {
        .img-area {
          overflow: hidden;
          height: 0;
          padding-bottom: 180 / 260 * 100 + %;
        }
      }
    }

    .carousel._2 {
      .carousel-btn {
        top: 120px;
      }

      .carousel-item {
        .img-area {
          overflow: hidden;
          height: 0;
          padding-bottom: 148%;
        }
      }
    }

    .carousel {
      // sm md
      @media(max-width: $superLarge) and (min-width: $small) {
        width: 80%;
        margin: 0 auto;
        width: calc(100% - 60px * 2);
      }

      &.mini {
        .carousel-item {
          margin-right: 0;
          .text-area{
            font-size: 25px;
            margin-top: 0;
            font-weight: 400;
          }
        }
        .slick-dots{
          margin-top: 20px;
        }
        .card{
          width: 100%;
        }
      }
      &._2{
        .carousel-item{
          .img-area{
            // width: 100%;
          }
        }
      }
    }
  }

  .subscribe-block {
    height: 445px;
    text-align: center;
    color: rgb(255, 255, 255);
    position: relative;
    overflow: hidden;
    // xs extra small 特小屏幕 手机
    @media(max-width: $small) {
      background: #4ababb;
    }
    .back-img{
      position: absolute;
      left: 0;
      top: 0;
      z-index: -1;
      width: 160%;
      // md medium 中等屏幕 桌面显示器
      @media(max-width: $large) and (min-width: $medium) {
        width: 200%;
      }
      // sm small 小屏幕 平板
      @media(max-width: $medium) and (min-width: $small) {
        width: 250%;
      }
    }
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

    form {
      margin-top: 80px;
    }

    ._fc {
      // form control
      $height: 70px;
      height: $height;
      line-height: $height;
      border-radius: 5px;
      font-size: 21px;
      padding: 0 25px;
      vertical-align: middle;
    }

    .input {
      @include noBb;
      background-color: rgb(255, 255, 255);
      width: 400px;
      color: $color1;
    }

    .btn {
      @include noBb;
      margin-left: 30px;
      background-color: rgb(38, 38, 38);
      font-weight: 500;
      text-transform: uppercase;

      &:focus,
      &:hover {
        color: #ccc;
      }
    }
    // xs sm
    @media(max-width: $medium) {
      .title {
        font-size: 40px;
      }

      .title2 {
        margin-top: 15px;
        font-size: 21px;
      }

      form {
        margin-top: 30px;

        ._fc {
          display: block;
          width: 350px;
          max-width: 90%;
          margin: 0 auto;
        }

        .input {
          margin-bottom: 15px;
        }
      }
    }
  }

}
</style>
