<template lang="pug">
.DatePicker.date-picker.form-group.has-feedback
  input.form-control.input-lg(type='text' :value="displayValue")
  span.icon.icon-calendar.form-control-feedback
  .mask(@click='togglePanel')
  //- .input-wrapper(@mouseenter='showCancel = true', @mouseleave='showCancel = false')
  //-   .input(@click='togglePanel', v-text="range ? value[0] + ' -- ' + value[1] : value")
  //-   transition(name='fade')
      //- img.cancel-btn(src='./cancel.png', v-show='showCancel', @click='clear')
  transition(name='toggle')
    .date-panel(v-show='panelState', :style='coordinates')
      .panel-header(v-show="panelType !== 'year'")
        .arrow-left(@click='prevMonthPreview()') &lt;
        .year-month-box
          .year-box(@click="chType('year')", v-text='tmpYear')
          .month-box(@click="chType('month')") {{tmpMonth + 1 | month(language)}}
        .arrow-right(@click='nextMonthPreview()') &gt;
      .panel-header(v-show="panelType === 'year'")
        .arrow-left(@click='chYearRange(0)') &lt;
        .year-range
          span(v-text='yearList[0]')
          |  -
          span(v-text='yearList[yearList.length - 1]')
        .arrow-right(@click='chYearRange(1)') &gt;
      .type-year(v-show="panelType === 'year'")
        ul.year-list
          li(v-for='item in yearList', v-text='item', :class="{selected: isSelected('year', item), invalid: validateYear(item)}", @click='selectYear(item)')
      .type-month(v-show="panelType === 'month'")
        ul.month-list
          li(v-for='(item, index) in monthList', :class="{selected: isSelected('month', index), invalid: validateMonth(index)}", @click='selectMonth(index)')
            | {{item | month(language)}}
      .type-date(v-show="panelType === 'date'")
        ul.weeks
          li(v-for='item in weekList') {{item | week(language)}}
        ul.date-list
          li(v-for='(item, index) in dateList', :class='{preMonth: item.previousMonth, nextMonth: item.nextMonth,\
          invalid: validateDate(item), firstItem: (index % 7) === 0}', @click='selectDate(item)')
            .message(:class="{selected: isSelected('date', item)}")
              .bg
              span(v-text='item.value')
</template>

<script>
import datepicker from 'vue-date'
import {format} from 'date-functions'
import {newDate} from '@/utils'

export default {
  extends: datepicker,
  props: {
    format: {default: 'yyyy-MM-dd'},
  },
  // components: {},
  // data() {
  //   return {}
  // },
  computed: {
    displayValue() {
      if (this.range) {
        const value = [this.formatValue(this.value[0]), this.formatValue(this.value[1])]
        return `${value[0]} -- ${value[1]}`
      } else {
        const value = this.formatValue(this.value)
        return value
      }
    },
  },
  // watch: {},
  methods: {
    formatValue(v) {
      return v ? format(newDate(v), this.format) : null
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.DatePicker{
  .mask{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
    ul{
        padding: 0;
        margin: 0;
        list-style: none;
    }
    .date-picker{
        position: relative;
        height: 32px;
    }
    .input-wrapper{
        border: 1px solid #ccc;
        border-radius: 2px;
        vertical-align: middle;
        display: flex;
        justify-content: space-between;
        flex-flow: row nowrap;
        align-items: center;
        padding: 6px 10px 6px 4px;
        height: 32px;
        box-sizing: border-box;
    }
    .input{
        height: 100%;
        width: 100%;
        font-size: inherit;
        padding-left: 4px;
        box-sizing: border-box;
        outline: none;
    }
    .cancel-btn{
        height: 14px;
        width: 14px;
    }
    .date-panel{
        position: absolute;
        z-index: 5000;
        border: 1px solid #eee;
        box-sizing: border-box;
        width: 320px;
        padding: 5px 10px 10px;
        box-sizing: border-box;
        background-color: #fff;
        transform: translateY(4px);
    }
    .panel-header{
        display: flex;
        flex-flow: row nowrap;
        width: 100%;
    }
    .arrow-left, .arrow-right{
        flex: 1;
        font-size: 20px;
        line-height: 2;
        background-color: #fff;
        text-align: center;
        cursor: pointer;
    }
    .year-range{
        font-size: 20px;
        line-height: 2;
        flex: 3;
        display: flex;
        justify-content: center;
    }
    .year-month-box{
        flex: 3;
        display: flex;
        flex-flow: row nowrap;
        justify-content: space-around;
    }
    .type-year, .type-month, .date-list{
        background-color: #fff;
    }
    .year-box, .month-box{
        transition: all ease .1s;
        font-family: Roboto, sans-serif;
        flex: 1;
        text-align: center;
        font-size: 20px;
        line-height: 2;
        cursor: pointer;
        background-color: #fff;
    }
    .year-list, .month-list{
        display: flex;
        flex-flow: row wrap;
        justify-content: space-between;
        li{
            font-family: Roboto, sans-serif;
            transition: all .45s cubic-bezier(0.23, 1, 0.32, 1) 0ms;
            cursor: pointer;
            text-align: center;
            font-size: 20px;
            width: 33%;
            padding: 10px 0;
            &:hover{
                background-color: #6ac1c9;
                color: #fff;
            }
            &.selected{
                background-color: #0097a7;
                color: #fff;
            }
            &.invalid{
                cursor: not-allowed;
                color: #ccc;
            }
        }
    }
    .date-list{
        display: flex;
        flex-flow: row wrap;
        justify-content: space-between;
        .valid:hover{
            background-color: #eee;
        }
        li{
            transition: all ease .1s;
            cursor: pointer;
            box-sizing: border-box;
            border-bottom: 1px solid #fff;
            position: relative;
            margin: 2px;
            &:not(.firstItem){
                margin-left: 10px;
            }
            .message{
                font-family: Roboto, sans-serif;
                font-weight: 300;
                font-size: 14px;
                position: relative;
                height: 30px;
                &.selected{
                    .bg{
                        background-color: rgb(0, 151, 167);
                    }
                    span{
                        color: #fff;
                    }
                }
                &:not(.selected){
                    .bg{
                        transform: scale(0);
                        opacity: 0;
                    }
                    &:hover{
                        .bg{
                            background-color: rgb(0, 151, 167);
                            transform: scale(1);
                            opacity: .6;
                        }
                        span{
                            color: #fff;
                        }
                    }
                }
                .bg{
                    height: 30px;
                    width: 100%;
                    transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms;
                    border-radius: 50%;
                    position: absolute;
                    z-index: 10;
                    top: 0;
                    left: 0;
                }
                span{
                    position: absolute;
                    z-index: 20;
                    left: 50%;
                    top: 50%;
                    transform: translate3d(-50%, -50%, 0);
                }
            }
            &.invalid{
                cursor: not-allowed;
                color: #ccc;
            }
        }

    }
    .weeks{
        display: flex;
        flex-flow: row wrap;
        justify-content: space-between;
        li{
            font-weight: 600;
        }
    }
    .weeks, .date-list{
        width: 100%;
        text-align: center;
        .preMonth, .nextMonth{
            color: #ccc;
        }
        li{
            font-family: Roboto;
            width: 30px;
            height: 30px;
            text-align: center;
            line-height: 30px;
        }
    }
    .toggle-enter, .toggle-leave-active{
        opacity: 0;
        transform: translateY(-10px);
    }
    .toggle-enter-active, .toggle-leave-active{
        transition: all ease .2s;
    }
    .fade-enter, .fade-leave-active{
        opacity: 0;
        transform: scale3d(0, 0, 0);
    }
    .fade-enter-active, .fade-leave-active{
        transition: all ease .1s;
    }
}
</style>
