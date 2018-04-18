<template lang="pug">
CardContainer.transaction
  .card-container-title Transaction
  .space
  .space
  .relative
    .search-area
      a.print(@click="print")
        Icon(name="printer")
      el-input.mlm(placeholder="Search" suffix-icon="el-icon-search")
    el-tabs.style-1(v-model='activeTab', type='card')
      el-tab-pane(label="All" name="All")
        Datatable(:cols="cols" :rows="rows")
          span(slot="appendHeadCell" slot-scope="props")
            template(v-if="props.col.name === 'paid'")
              QuestionCircle.mls
          span(slot="appendCell" slot-scope="props")
            template(v-if="props.col.name === 'course_fee'")
              .fee-detail
                el-tooltip.item(content="Accomodation: 10000", placement='bottom')
                  Icon.accomodation-icon(name="bed")
                el-tooltip.item(content="Insurance: 10000", placement='bottom')
                  Icon.insurance-icon(name="insurance")
                el-tooltip.item(content="Down Payment: 10000", placement='bottom')
                  Icon.downpayment-icon(name="downpayment")
          .refund-request(slot="cell" slot-scope="props")
            span(v-if="props.col.name === 'refund_request'")
              template(v-if="props.value==='pending'")
                el-button(type="primary") Refund
                el-button(type="danger") Reject
              template(v-else-if="props.value==='refunded'") ${{props.row.paid}} Refunded
              span.text-danger.bold(v-else) Rejected
            span(v-else) {{props.value}}
          th(slot="appendHead")
          td.actions(slot="appendRow"  slot-scope="props")
            el-dropdown(trigger="click")
              .actions-btn
                | Actions
                span.caret.mls
              el-dropdown-menu(slot="dropdown" class="actions-dropdown")
                el-dropdown-item
                  a
                    Icon(name="dialog")
                    span Message
                el-dropdown-item(divided)
                  a
                    Icon(name="refund")
                    span Refund
                el-dropdown-item(divided)
                  a
                    Icon(name="trash")
                    span Delete
      el-tab-pane(label="Paid" name="Paid")
      el-tab-pane(label="Refund Request" name="Refund Request")
      el-tab-pane(label="Cancelled" name="Cancelled")
</template>

<script>
import CardContainer from '@/components/CardContainer'
import Datatable from '@/components/Datatable'
// import Tooltip from '@/components/Tooltip'

const statusClassMapping = {
  paid: 'text-success',
  cancelled: 'text-danger',
  refund: 'text-primary',
}

export default {
  components: {CardContainer, Datatable},
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
.transaction{
  // text color
  .text-success {
    color: #6ca153;
  }
  .text-primary {
    color: #2a97cf;
  }
  .text-danger {
    color: #ff0404;
  }
  .text-warning {
    color: #f39d00;
  }
  .bold{
    font-weight: bold;
  }
  .search-area{
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
        font-size: 24px;
      }
    }
  }
  .paid{
    .icon{
      font-size: 18px;
      color: #fff;
    }
  }
  .course-fee{
    white-space: nowrap;
  }
  .fee-detail{
    display: inline-block;
    margin-left: 20px;
    .icon{
      cursor: pointer;
      display: inline-block;
      $side: 25px;
      width: $side;
      height: $side;
      line-height: $side;
      text-align: center;
      font-size: 18px;
      color: #fff;
      border-radius: 3px;
      margin-right: .2em;
    }
  }
  .refund-request{
    display: inline-block;
    white-space: nowrap;
    .el-button{
      padding: 3px 8px;
      font-size: 12px;
    }
  }
  .actions-btn{
    cursor: pointer;
    display: inline-block;
    white-space: nowrap;
    .caret{
      margin-left: .5em;
    }
  }
}
.actions-dropdown{
  .icon{
    display: inline-block;
    width: 1.8em;
    position: relative;
    font-size:12px;
  }
}
</style>
