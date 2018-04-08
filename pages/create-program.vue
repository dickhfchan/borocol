<template lang="pug">
CardContainer.create-program
  .page0.text-center.pal(v-if="page===0")
    .title I want to create
    ._1
      b.text-box(:class="{active:pages[0].withAccom}" @click="pages[0].withAccom=true") A Program<br>"With" Accomodation <QuestionCircle/>
      .or OR
      b.text-box(:class="{active:!pages[0].withAccom}" @click="pages[0].withAccom=false") A Program<br>"Without" Accomodation <QuestionCircle/></span>
    ._2
      el-checkbox(v-model="pages[0].agreed")
      span.mls I acknowledge that Borocol will take service charge (13%) on per succesful application. I hereby agree to “<a><b>Terms of Service</b></a>” and understanding the purpose of collecting personal data.
    .mtl
    el-button.confirm-btn(type="primary" size="large" @click="page0confirm") Confirm
  div(v-else :class="'page' + page")
    .cp-header
      .step Step {{pageCur.step}}
      .title {{pageCur.title}}
    el-progress(:text-inside='true', :stroke-width='20', :percentage="progress", color="#fc0")
    .cp-body
      el-row(:gutter="80")
        el-col(:sm="15" :md="16" :lg="17")
          div(v-if="page===1")
            el-row(:gutter="16")
              el-col.mbm(:md="8")
                FormItem(:field="pageCur.fields.startDate")
                  el-date-picker(slot="control" type="date"
                    v-model="pageCur.fields.startDate.value"
                  )
              el-col.mbm(:md="8")
                FormItem(:field="pageCur.fields.endDate")
                  el-date-picker(slot="control" type="date"
                    v-model="pageCur.fields.endDate.value"
                  )
              el-col.mtl.hidden-sm-and-down
              el-col.mbm(:md="15")
                FormItem(:field="pageCur.fields.categoryId" type="select")
              el-col.mbm(:md="9")
                FormItem(:field="pageCur.fields.level" type="select")
              el-col.mtl.hidden-sm-and-down
              el-col.mbm(:md="25")
                FormItem(:field="pageCur.fields.title")
          div(v-else-if="page===2")
            el-row(:gutter="16")
              el-col.mbm(:md="8")
                FormItem(:field="pageCur.fields.gender" type="select")
              el-col.mbm(:md="16")
                FormItem(:field="pageCur.fields.ageRange")
                  el-slider(slot="control" range :min="16" :max='100'
                    v-model="pageCur.fields.ageRange.value"
                  )
              el-col.mtl.hidden-sm-and-down
              el-col.mbm
                FormLabel(:field="pageCur.fields.timeRange")
                .time-range.mlm
                  el-input(v-model="pageCur.fields.timeRange.value[0]" type="number")
                  .divider -
                  el-input(v-model="pageCur.fields.timeRange.value[1]" type="number")
              el-col.mtl.hidden-sm-and-down
              el-col.mbm
                FormItem(:field="pageCur.fields.description" type="textarea"
                  :controlAttrs="{rows:8}"
                )

        el-col.hidden-xs-only(:sm="9" :md="8" :lg="7")
          .cp-tips
            .tip
              .tip-title
                Icon(name="idea")
                | Tips
              .tip-text {{pageCur.tips && pageCur.tips[0] || 'More information more chance to attract your student!'}}
            .tip.mtl
              .tip-title
                Icon(name="idea")
                | Tips
              .tip-text {{pageCur.tips && pageCur.tips[1] || 'More information more chance to attract your student!'}}
          .cp-actions.mtl
            a.cp-action(@click="page--") Back
            a.cp-action.cp-action-next(@click="page++")
              Icon(name="arrow-right")
</template>

<script>
import CardContainer from '@/components/CardContainer'
import ImageUploader from '@/components/ImageUploader';
import NationSelect from '@/components/NationSelect';
import * as ut from '@/plugins/utils'

export default {
  components: {CardContainer, ImageUploader, NationSelect},
  data() {
    return {
      page: 2,
      pages: [
        {
          withAccom: true,
          agreed: false,
        },
        {
          step: 1,
          title: 'Start with the basic 1.1',
          tips: [null, 'Create a title that can attract people’s attention. '],
          fields: {
            startDate: {text: 'Start Date', rules: 'required'},
            endDate: {text: 'End Date', rules: 'required'},
            categoryId: {text: 'Category', rules: 'required'},
            level: {text: 'Level', rules: 'required'},
            title: {text: 'Create an Attractive Title', nameInMessage: 'title', rules: 'required'},
          },
        },
        {
          step: 2,
          title: 'Start with the basic 1.2',
          fields: {
            gender: {text: 'Gender', rules: 'required'},
            ageRange: {text: 'Age', value: [16, 32]},
            timeRange: {text: 'How many hour will It take to complete this program?',
              nameInMessage: 'Time Range', rules: 'required', value:[null, null]}, // todo validate
            description: {text: 'Description of the program (What we will do)', nameInMessage: 'description', rules: 'required'},
          },
        },
      ],
    }
  },
  computed: {
    pageCur() { return this.pages[this.page] },
    progress() { return Math.floor(this.page / (this.pages.length - 1) * 100) },
  },
  // watch: {},
  methods: {
    page0confirm() {
      if (!this.pages[0].agreed) {
        this.$alert('Please accept the terms.')
      } else {
        this.page++
      }
    },
  },
  // created() {},
  mounted() {
    this.$watch('page', (i) => {
      const page = this.pages[i]
      if (page.fields) {
        this.$set(page, 'validation', {})
        this.$validate(page.validation, page.fields)
      }
    }, {immediate: true})
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.create-program{
  .form-label {
    font-weight: bold;
  }
  .el-card__body{
    padding: 0;
  }
  .el-progress-bar__outer{
    border-radius: 0;
  }
  .el-progress-bar__inner{
    text-align: center;
    border-radius: 0;
  }
  .el-progress-bar__innerText{
    font-weight: 500;
    color: #333;
  }
}
.cp-header{
  font-size: 28px;
  $h: 80px;
  height: $h;
  line-height: $h;
  .step{
    display: inline-block;
    font-weight: bold;
    width: 170px;
    text-align: center;
    color: darken($primaryColor, 10%);
  }
  .title{
    display: inline-block;
    padding-left: 30px;
  }
}
.cp-body{
  padding: 50px 100px;
}
.cp-tips{
  .tip{
    border-width: 2px;
    border-color: #ddd;
    border-style: solid;
    border-radius: 3px;
    padding: 15px 20px;
  }
  .tip-title{
    font-size: 22px;
    .icon{
      font-size: 28px;
      margin-right: 15px;
    }
  }
  .tip-text{
    margin-top: 20px;
    color: #888;
    line-height: 25px;
  }
}
.cp-actions{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.cp-action{
  color: #333;
  font-size: 28px;
  &:hover{
    text-decoration: none;
  }
}
.cp-action-next{
  .icon{
    font-size: 36px;
  }
}
.page0{
  .title{
    font-size: 40px;
    font-weight: 500;
    margin-bottom: 80px;
  }

  ._1 {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .text-box{
    width: 320px;
    font-size: 18px;
    display: inline-block;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    cursor: pointer;
    &:hover{
      background: #f7f7f7;
    }
    &.active{
      border-color: #888;
    }
  }
  .or{
    display: inline-block;
    height: 100%;
    line-height: 100%;
    vertical-align: middle;
    padding: 30px;
  }
  ._2{
    text-align: left;
    width: 70%;
    display: flex;
    margin: 0 auto;
    margin-top: 30px;
    font-size: 15px;
  }
  // xs extra small 特小屏幕 手机
  @media(max-width: $small) {
    ._1{
      display: block;
    }
    .text-box{
      display: block;
      width: auto;
    }
  }
}
.page1{}
.page2{}
.time-range{
  display: inline-block;
  .el-input{
    display: inline-block;
    width: 80px;
  }
  .divider{
    display: inline-block;
    width: 1.6em;
    text-align: center;
  }
}
</style>
