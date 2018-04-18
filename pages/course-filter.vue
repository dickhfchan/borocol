<template lang="pug">
.course-filter.container
  .space
  .space
  .space
  el-breadcrumb(separator='/')
    el-breadcrumb-item(:to="{name: 'index'}") Home
    el-breadcrumb-item Search Result
  .space
  .space
  .toolbar
    el-dropdown(trigger='click')
      el-button Course Status
        span.mlm
        span.caret
      el-dropdown-menu.cf-toolbar-dropdown-menu(slot='dropdown')
        .line
          el-checkbox
          span.mls Most Viewd
        .line
          el-checkbox
          span.mls Featuved Course
        .line
          el-checkbox
          span.mls Early Bird
        .line
          el-checkbox
          span.mls Soon to Start
    el-dropdown.mls(trigger='click')
      el-button Level
        span.mlm
        span.caret
      el-dropdown-menu.cf-toolbar-dropdown-menu(slot='dropdown')
        .line
          el-checkbox
          span.mls All
        .line
          el-checkbox
          span.mls Beginner
        .line
          el-checkbox
          span.mls Intermediate
        .line
          el-checkbox
          span.mls Upper Intermediate
        .line
          el-checkbox
          span.mls Advanced
    el-dropdown.mls(trigger='click')
      el-button Durauon
        span.mlm
        span.caret
      el-dropdown-menu.cf-toolbar-dropdown-menu(slot='dropdown')
        .line
          el-checkbox
          span.mls All
        .line
          el-checkbox
          span.mls 1 day only
        .line
          el-checkbox
          span.mls less than 1 week
        .line
          el-checkbox
          span.mls 1-4 weeks
        .line
          el-checkbox
          span.mls 1 month or above
    el-date-picker.date-picker.mls(
      v-model="startDate"
      type="date" placeholder="Course Start Date"
    )
    el-date-picker.date-picker.mls(
      v-model="endDate"
      type="date" placeholder="Course End Date"
    )
    el-input.search(placeholder="Key Words Search" suffix-icon="el-icon-search")
  .space
  .space
  .space
  Row(:gutter="40")
    Col(:span="6" :width="350")
      img.w-100(src="https://picsum.photos/500/400?image=401")
      .form-group.mtl
        label Categories
        el-select(v-model="category")
          el-option(value="") Language - Japanese
      .form-group.mtl
        label Countries
        el-select(v-model="countries")
          el-option(value="") Japan - Tokyo
      .price-filter.flex.align-c
        .mrs Price
        .flex-1
          el-slider(range v-model="priceRange" :min="0" :max="100000")
      .el-checkbox-filters.mtl
        el-checkbox
        Icon.mls(name="female")
        span.mls Female Only
        el-checkbox.mll
        Icon.mls(name="male")
        span.mls Male Only
        br
        el-checkbox
        span.mls Accomodation
    Col(:span="6" :width="500" :grow="1")
      .course-card2.course-card2-result
        .course-card2__img-area(href="#")
          AspectImage(src="https://picsum.photos/500/300?image=407" :aspect="1.7")
          .mark Early Bird Sale
          .course-card2__collect
            Icon(name="heart-o")
          el-button.share-btn
            Icon.mrs(name="share")
            | Share
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
          .course-card2__title Private English Tutor in Monaco: 10 Private English Lessons Pevat...
          .mtl
            .line.mbs
              Icon.course-card2__key-icon(name="graduation-hat")
              span Connect Enghsh Language \nstwtuter Mwsswon VaHey
            .line.mbs
              Icon.course-card2__key-icon(name="position")
              span SAN D‘EGO‘ USA
            .line.mbs
              Icon.course-card2__key-icon(name="locale")
              span Offered m Japanese
            .line.mbs
              Icon.course-card2__key-icon(name="calendar")
              span Feb 20‘ 16 , Mar 30‘ 17
          .course-card2__prices
            .course-card2__price USD 600,000
            .course-card2__oprice Original: $700,000
          el-button.view-btn(type="primary" size="large") View Details
      .course-card2.course-card2-result
        .course-card2__img-area(href="#")
          AspectImage(src="https://picsum.photos/500/300?image=408" :aspect="1.7")
          .mark Early Bird Sale
          .course-card2__collect
            Icon(name="heart-o")
          el-button.share-btn
            Icon.mrs(name="share")
            | Share
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
          .course-card2__title Private English Tutor in Monaco: 10 Private English Lessons Pevat...
          .mtl
            .line.mbs
              Icon.course-card2__key-icon(name="graduation-hat")
              span Connect Enghsh Language \nstwtuter Mwsswon VaHey
            .line.mbs
              Icon.course-card2__key-icon(name="position")
              span SAN D‘EGO‘ USA
            .line.mbs
              Icon.course-card2__key-icon(name="locale")
              span Offered m Japanese
            .line.mbs
              Icon.course-card2__key-icon(name="calendar")
              span Feb 20‘ 16 , Mar 30‘ 17
          .course-card2__prices
            .course-card2__price USD 600,000
            .course-card2__oprice Original: $700,000
          el-button.view-btn(type="primary" size="large") View Details
      .related-title.mvl.pvl Similar Courses
      el-row(:gutter="16").related.mtl
        el-col(:span="12")
          .course-card2
            .course-card2__img-area(href="#")
              AspectImage(src="https://picsum.photos/500/300?image=408" :aspect="1.7")
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
        el-col(:span="12")
          .course-card2
            .course-card2__img-area(href="#")
              AspectImage(src="https://picsum.photos/500/300?image=409" :aspect="1.7")
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
        el-col(:span="12")
          .course-card2
            .course-card2__img-area(href="#")
              AspectImage(src="https://picsum.photos/500/300?image=400" :aspect="1.7")
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
        el-col(:span="12")
          .course-card2
            .course-card2__img-area(href="#")
              AspectImage(src="https://picsum.photos/500/300?image=401" :aspect="1.7")
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
</template>

<script>
export default {
  components: {},
  data() {
    return {
      startDate: null,
      endDate: null,
      category: null,
      countries: null,
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
@import "~assets/style/global.scss";
@import "~assets/style/course-card2.scss";
.cf-toolbar-dropdown-menu{
  padding: 10px;
  font-size: 13px;
  line-height: 25px;
  white-space: nowrap;
}
.course-filter{
  .justify-sb {
    justify-content: space-between;
  }

  .justify-c {
    justify-content: center;
  }
  .align-c{
    align-items: center;
  }
  .toolbar{
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
    .date-picker{
      width: 200px;
      display: inline-block;
      vertical-align: top;
    }
    .search{
      width: 350px;
      float: right;
    }
  }
  .price-filter{
    margin-top: 50px;
  }
  .el-checkbox-filters{
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
  .course-card2-result{
    display: flex;
    .course-card2__img-area{
      width: 480px;
      flex-shrink: 0;
    }
    .course-card2__text-area{
      position: relative;
      padding: 15px;
      margin-left: 10px;
    }
    .course-card2__key-icon{
      width: 25px;
      display: inline-block;
      color: #ccc;
      font-size: 18px;
    }
    .course-card2__prices{
      position: absolute;
      bottom: 10px;
    }
    .course-card2__price{
      font-size: 18px;
      font-weight: bold;
      color: $primaryColor;
    }
    .course-card2__oprice{
      text-decoration: line-through;
    }
    .view-btn{
      position: absolute;
      bottom: 10px;
      right: 10px;
      padding: 15px 20px;
    }
  }
  .related-title {
      font-size: 18px;
      font-weight: 500;
      text-align: center;
  }
}
</style>
