<template lang="pug">
include ../common.pug
.Orders
  .container
    .content-card
      h1.content-card-title Orders
      .content-card-body
        Tabs(v-model="activeTab")
          ._1
            a.print(href="javascript:void(0)" @click="print")
              span.icon.icon-printer
            .search.input-with-icon
              +input(placeholder="Search")
              span.icon.icon-search
          Tab.mtl(name="All")
            Datatable(:cols="cols" :rows="rows")
              span(slot="appendHeadCell" slot-scope="props")
                template(v-if="props.col.name === 'paid'")
                  span.mls.icon.icon-question-circle
              span(slot="appendCell" slot-scope="props")
                template(v-if="props.col.name === 'course_fee'")
                  .fee-detail
                    Tooltip(title="Accomodation: 10000")
                      span.accomodation.icon.icon-accommodation
                    Tooltip(title="Insurance: 10000")
                      span.insurance.icon.icon-insurance
                    Tooltip(title="Down Payment: 10000")
                      span.downpayment.icon.icon-downpayment
              .refund-request(slot="cell" slot-scope="props")
                span(v-if="props.col.name === 'refund_request'")
                  template(v-if="props.value==='pending'")
                    button.btn.btn-primary.btn-sm(type="button") Refund
                    .space
                    button.btn.btn-danger.btn-sm(type="button") Reject
                  template(v-else-if="props.value==='refunded'") ${{props.row.paid}} Refunded
                  span.text-danger.bold(v-else) Rejected
                span(v-else) {{props.value}}
              th(slot="appendHead")
              td.actions(slot="appendRow"  slot-scope="props")
                .dropdown.left
                  .actions-btn
                    | Actions
                    span.caret.mls
                  ul.dropdown-menu
                    li
                      a(href="javascript:void(0)")
                        span.icon.icon-talk
                        | Message
                    li.divider
                    li
                      a(href="javascript:void(0)")
                        span.icon.icon-refund
                        | Refund
                    li.divider
                    li
                      a(href="javascript:void(0)")
                        span.icon.icon-trash-o
                        | Delete
          Tab(name="Paid") Paid
          Tab(name="Refund Request") Refund Request
          Tab(name="Cancelled") Cancelled
</template>

<script>
import Tabs from '@/components/Tabs'
import Tab from '@/components/Tab'
import Datatable from '@/components/Datatable'
import Tooltip from '@/components/Tooltip'

const statusClassMapping = {
  paid: 'text-success',
  cancelled: 'text-danger',
  refund: 'text-primary',
}

export default {
  components: {Tabs, Tab, Datatable, Tooltip},
  data() {
    return {
      activeTab: 'All',
      cols: [
        {
          "text": "Thansaction No.",
          "name": "thansaction_no"
        },
        {
          "text": "Status",
          "name": "status",
          getCellClass: ({value}) => `${statusClassMapping[value]} bold`,
        },
        {
          "text": "Student Name",
          "name": "student_name",
          getCellClass: ({value}) => `text-warning bold`,
        },
        {
          "text": "Course ID",
          "name": "course_id"
        },
        {
          "text": "Course Name",
          "name": "course_name",
          getCellClass: ({value}) => `bold`,
        },
        {
          "text": "Course fee",
          "name": "course_fee",
          getCellClass: () => 'course-fee',
        },
        {
          "text": "Paid",
          "name": "paid",
          getHeadClass: () => 'paid',
        },
        {
          "text": "Paid on",
          "name": "paid_on"
        },
        {
          "text": "Refund Request",
          "name": "refund_request"
        },
      ],
      rows: [
        {
          thansaction_no: '#10001',
          status: 'paid',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'refunded',
        },
        {
          thansaction_no: '#10001',
          status: 'cancelled',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'pending',
        },
        {
          thansaction_no: '#10001',
          status: 'refund',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'pending',
        },
        {
          thansaction_no: '#10001',
          status: 'paid',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'rejected',
        },
        {
          thansaction_no: '#10001',
          status: 'paid',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'refunded',
        },
        {
          thansaction_no: '#10001',
          status: 'cancelled',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'pending',
        },
        {
          thansaction_no: '#10001',
          status: 'refund',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'pending',
        },
        {
          thansaction_no: '#10001',
          status: 'paid',
          student_name: 'Kayla Wong',
          course_id: '#1000000',
          course_name: 'Accelerated English Course ...',
          course_fee: '10000',
          paid: '10000',
          paid_on: 'May 24, 2017',
          refund_request: 'rejected',
        },
      ],
    }
  },
  // computed: {},
  // watch: {},
  methods: {
    print() {}
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.Orders{
  background-image: url(~@/assets/img/orders-bg.jpg);
  background-size: 100%;
  @media(max-width: 1920px) {
    background-size: 1920px;
  }
  .container{
    width: 1400px;
    padding: 0;
  }
  .Tabs{
    position: relative;
  }
  ._1{
    position: absolute;
    top: -20px;
    right: 0;
    display: flex;
    align-items: center;
    a.print{
      text-decoration: none;
      font-size: 25px;
      color: #000;
      .icon {

      }
    }
    .search{
      margin-left: 1em;
      .icon{
        top: 7px;
      }
    }
  }
  .bold{
    font-weight: bold;
  }
  .paid{
    .icon{
      position: relative;
      top: -2px;
    }
  }
  .course-fee{
    white-space: nowrap;
  }
  .fee-detail{
    display: inline-block;
    margin-left: 20px;
    .Tooltip{
      margin-left: .25em;
    }
    span{
      display: inline-block;
      width: 25px;
      height: 25px;
      line-height: 25px;
      text-align: center;
      font-size: 18px;
      color: #fff;
      border-radius: 3px;
    }
  }
  .accomodation{
    background: #968ecb;
  }
  .insurance{
    background: #63cace;
  }
  .downpayment{
    background: #a6c875;
    &:before{
      position: relative;
      top: -2px;
    }
  }
  .refund-request{
    display: inline-block;
    white-space: nowrap;
    .btn{
      padding: 3px 8px;
    }
  }
  .actions-btn{
    display: inline-block;
    white-space: nowrap;
    .caret{
      margin-left: .5em;
    }
  }
  .actions{
    .dropdown{
      .icon{
        display: inline-block;
        width: 1.5em;
        position: relative;
        top: -1px;
      }
    }
  }
}
</style>
