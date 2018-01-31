<template lang="pug">
include ../common.pug
.CourseFilter
  .container
    .breadcrumb
      li
        a(href="javascript:void(0)") Home
      li.active Search Result
    .toolbar.mtl
      .dropdown
        button.btn.btn-default Course Status
          span.caret.mls
        .dropdown-menu
          .line
            Checkbox
            span.mls Most Viewd
          .line
            Checkbox
            span.mls Featuved Course
          .line
            Checkbox
            span.mls Early Bird
          .line
            Checkbox
            span.mls Soon to Start

      .dropdown.mls
        button.btn.btn-default Level
          span.caret.mls
        .dropdown-menu
          .line
            Checkbox
            span.mls All
          .line
            Checkbox
            span.mls Beginner
          .line
            Checkbox
            span.mls Intermediate
          .line
            Checkbox
            span.mls Upper Intermediate
          .line
            Checkbox
            span.mls Advanced
      .dropdown.mls
        button.btn.btn-default Durauon
          span.caret.mls
        .dropdown-menu
          .line
            Checkbox
            span.mls All
          .line
            Checkbox
            span.mls 1 day only
          .line
            Checkbox
            span.mls less than 1 week
          .line
            Checkbox
            span.mls 1-4 weeks
          .line
            Checkbox
            span.mls 1 month or above
      DatePicker.mls(placeholder="Course Start Date")
      DatePicker.mls(placeholder="Course End Date")
      .search.input-with-icon
        +inputLg(placeholder="Key Words Search")
        span.icon.icon-search
    el-row.mtl(:gutter="40")
      el-col(:span="6")
        img.w-100(src="https://picsum.photos/500/400?image=401")
        .form-group.mtl
          label Categories
          +selectLg
            option Language - Japanese
        .form-group.mtl
          label Conntries
          +selectLg
            option Japan - Tokyo
        .price-filter.flex
          .mrs Price
          Slider.flex-1(v-model="priceRange" :min="0" :max="100000")
        .checkbox-filters.mtl
          Checkbox
          span.icon.icon-female.mls
          span.mls Female Only
          Checkbox.mll
          span.icon.icon-male.mls
          span.mls Male Only
          br
          Checkbox
          span.mls Accomodation
      el-col(:span="18")
        .course-card.course-card-result
          a.course-card__img-area(href="#")
            img.img(src="https://picsum.photos/500/300?image=407")
            .mark Early Bird Sale
            .course-card__collect
              span.icon.icon-heart-o
            button.share-btn.btn.btn-primary.btn-sm
              span.icon.icon-share.mrs
              | Share
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
            .course-card__title Private English Tutor in Monaco: 10 Private English Lessons Pevat...
            .mtl
              .line.mbs
                span.course-card__key-icon.icon.icon-graduation-hat
                span Connect Enghsh Language \nstwtuter Mwsswon VaHey
              .line.mbs
                span.course-card__key-icon.icon.icon-position
                span SAN D‘EGO‘ USA
              .line.mbs
                span.course-card__key-icon.icon.icon-language
                span Offered m Japanese
              .line.mbs
                span.course-card__key-icon.icon.icon-calendar
                span Feb 20‘ 16 , Mar 30‘ 17
            .flex.justify-sb.mts
              .course-card__date Feb 20,16 , Mar 30,17
            .course-card__prices
              .course-card__price USD 600,000
              .course-card__oprice Original: $700,000
            button.view-btn.btn.btn-primary.btn-md View Details
        .course-card.course-card-result
          a.course-card__img-area(href="#")
            img.img(src="https://picsum.photos/500/300?image=407")
            .mark Early Bird Sale
            .course-card__collect
              span.icon.icon-heart-o
            button.share-btn.btn.btn-primary.btn-sm
              span.icon.icon-share.mrs
              | Share
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
            .course-card__title Private English Tutor in Monaco: 10 Private English Lessons Pevat...
            .mtl
              .line.mbs
                span.course-card__key-icon.icon.icon-graduation-hat
                span Connect Enghsh Language \nstwtuter Mwsswon VaHey
              .line.mbs
                span.course-card__key-icon.icon.icon-position
                span SAN D‘EGO‘ USA
              .line.mbs
                span.course-card__key-icon.icon.icon-language
                span Offered m Japanese
              .line.mbs
                span.course-card__key-icon.icon.icon-calendar
                span Feb 20‘ 16 , Mar 30‘ 17
            .flex.justify-sb.mts
              .course-card__date Feb 20,16 , Mar 30,17
            .course-card__prices
              .course-card__price USD 600,000
              .course-card__oprice Original: $700,000
            button.view-btn.btn.btn-primary.btn-md View Details
        .related-title.mvl.pvl Similar Courses
        el-row(:gutter="16").related.mtl
          el-col(:span="12")
            .course-card
              a.course-card__img-area(href="#")
                img.img(src="https://picsum.photos/500/300?image=408")
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
          el-col(:span="12")
            .course-card
              a.course-card__img-area(href="#")
                img.img(src="https://picsum.photos/500/300?image=400")
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
                img.img(src="https://picsum.photos/500/300?image=401")
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
</template>

<script>
import Slider from '@/components/Slider';
import DatePicker from '@/components/DatePicker';
export default {
  components: {Slider, DatePicker},
  data() {
    return {
      priceRange: [0, 50000],
    }
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
.CourseFilter{
  .container {
    width: 1385px;
    margin: 40px auto 140px auto;
  }
  .toolbar{
    .dropdown-menu{
      padding: 10px;
      font-size: 13px;
      line-height: 25px;
      white-space: nowrap;
    }
    .btn{
      text-transform: capitalize;
      height: 46px;
      line-height: 46px;
      padding: 0 20px;
      .caret{
        display: inline-block;
        margin-left: 30px;
      }
    }
    .DatePicker{
      width: 200px;
      display: inline-block;
      vertical-align: top;
    }
    .search{
      width: 400px;
      float: right;
    }
  }
  .price-filter{
    margin-top: 50px;
  }
  .checkbox-filters{
    line-height: 40px;
  }
  .icon-male{
    font-size: 20px;
    color: rgb(80, 183, 242);
  }
  .icon-female{
    font-size: 20px;
    color: rgb(255, 87, 116);
  }
  // right
  .course-card-result{
    display: flex;
    .course-card__img-area{
      width: 480px;
      flex-shrink: 0;
    }
    .course-card__text-area{
      position: relative;
      padding: 15px;
      margin-left: 10px;
    }
    .course-card__key-icon{
      width: 25px;
      display: inline-block;
      color: #ccc;
      font-size: 18px;
    }
    .course-card__prices{
      position: absolute;
      bottom: 10px;
    }
    .course-card__price{
      font-size: 18px;
      font-weight: bold;
      color: $bg2;
    }
    .course-card__oprice{
      text-decoration: line-through;
    }
    .view-btn{
      position: absolute;
      bottom: 10px;
      right: 10px;
    }
  }
}
</style>
