import Vue from 'vue'
import {snakeCase} from 'helper-js'
import store from './index'
import {createCourse as routes} from '@/routes/index'
import {steps} from '@/initialData'
import {newDate} from '@/utils'

const priceRegex = /^[1-9]\d*(\.\d{1,2})?$/
const requiredIfRoomEnabled1 = ({fields}) => fields.room1Enabled.value
const requiredIfRoomEnabled2 = ({fields}) => fields.room2Enabled.value

const state = {
  routes,
  ignoreValidation: false, // only when developing
  steps,
  fields: [
    // 0
    {
      declared: {
        rules: 'required|accepted',
      },
      agreed: {
        rules: 'required|accepted',
      },
    },
    // 1
    {
      name: {
        rules: 'required',
        text: 'Title',
      },
      category_id: {
        rules: 'required',
        text: 'Category',
      },
      level: {
        rules: 'required',
        text: 'Level',
      },
      startDate: {
        rules: 'required',
        text: 'Start Date',
      },
      endDate: {
        rules: 'required',
        text: 'End Date',
      },
      description: {
        rules: '',
        text: 'What Will We Do? (Description)',
      },
    },
    // 2
    {
      groupSize: {
        rules: 'required',
        text: 'Group Size',
      },
      gender: {
        rules: '',
        text: 'Gender',
        options: [
          {value: 'male', text: 'Male'},
          {value: 'female', text: 'Female'},
        ],
        enum: true,
      },
      ageRange: {
        text: 'Age',
        value: [16, 32],
      },
      hours: {
        rules: 'required',
      },
      language: {
        rules: 'required',
      },
      instructorPhoto: {},
      instructorInfo: {},
      issueCertificate: {
        rules: 'required',
        value: false,
      },
      certificate: {},
    },
    // 3
    {
      address: {
        rules: 'required',
        text: 'Address',
      },
      city: {
        rules: 'required',
        text: 'City',
      },
      country: {
        rules: 'required',
        text: 'Country',
      },
      apiKey: {
        rules: 'required',
        text: 'API Key',
      },
      locationDescription: {
        rules: '',
        text: 'Describe the location',
      },
      howToGetThere: {
        rules: '',
        text: 'How to get there?',
      },
      whereToMeet: {
        rules: '',
        text: 'Where to meet up your guest?',
      },
    },
    // 4
    {
      schedule: {
        rules: 'required',
        text: 'Itinerary / Typical Daily Schedule',
        nameInMessage: 'schedule',
      },
      mealsIncluded: {
        rules: 'required',
        text: 'Are meals included?',
        value: false,
      },
      meals: {
        rules: '',
        value: [],
      },
      mealsInfo: {
        rules: '',
      },
    },
    // 5
    {
      provide: {
        rules: '',
        text: 'What You’ll Provide?',
      },
      guestNeedsToBring: {
        rules: '',
        text: 'What Your Guest Needs to Bring?',
      },
    },
    // 6
    {
      guestRequirement: {
        rules: '',
        text: 'Guest Requirement',
      },
      requestFormExisted: {
        rules: 'required',
        text: 'Do you want to set up a Request Form?',
        value: false,
      },
      requestForm: {
        value: [{enabled: false, value: null}, {enabled: false, value: null}],
        type: 'json',
      },
    },
    // 7
    {
      tags: {
        rules: '',
        text: 'Tags',
        value: [],
      },
      cover: {
        rules: 'required',
        text: 'Cover Photo',
      },
      photos: {
        rules: 'required|minLength:2',
        text: 'Photos (Min. 3)',
        nameInMessage: 'photos',
        value: [],
      },
      notes: {
        text: 'Notes',
      },
    },
    // 8
    {
      options: {
        rules: '',
        value: [],
      },
      otherOptions: {
        rules: 'requiredIf',
        text: 'Other Options',
        ruleParams: {
          requiredIf: ({fields}) => fields.options.value.includes('others')
        },
      },
      locationDescription: {
        text: 'Describe the location',
      },
      facilities: {
        text: 'Facilities',
        value: [],
      },
      otherFacilities: {
        rules: 'requiredIf',
        text: 'Other Facilities',
        ruleParams: {
          requiredIf: ({fields}) => fields.facilities.value.includes('others')
        },
      },
      photos: {
        rules: '',
        text: 'Upload Photos (If Any)',
        value: [],
      },
      room1Enabled: {},
      room1Type: {
        rules: 'requiredIf',
        text: 'Room Type',
        ruleParams: {
          requiredIf: [requiredIfRoomEnabled1],
        },
      },
      room1Quota: {
        rules: 'requiredIf',
        text: 'Room Quota',
        ruleParams: {
          requiredIf: [requiredIfRoomEnabled1],
        },
      },
      room1Price: {
        rules: 'requiredIf|regex',
        ruleParams: {
          requiredIf: [requiredIfRoomEnabled1],
          regex: [priceRegex]
        },
        nameInMessage: 'Room Price',
      },
      room2Enabled: {},
      room2Type: {
        rules: 'requiredIf',
        text: 'Room Type',
        ruleParams: {
          requiredIf: [requiredIfRoomEnabled2],
        },
      },
      room2Quota: {
        rules: 'requiredIf',
        text: 'Room Quota',
        ruleParams: {
          requiredIf: [requiredIfRoomEnabled2],
        },
      },
      room2Price: {
        rules: 'requiredIf|regex',
        ruleParams: {
          requiredIf: [requiredIfRoomEnabled2],
          regex: [priceRegex]
        },
        nameInMessage: 'Room Price',
      },
    },
    // 9
    {
      seats: {
        rules: 'required|integer',
        text: 'How many seats available on Borocol',
        nameInMessage: 'seats',
      },
      price: {
        rules: 'required|regex',
        ruleParams: {
          regex: [priceRegex]
        },
        text: 'Price (13% service charge is included)',
        nameInMessage: 'price',
      },
      registrationStartDate: {
        rules: 'required',
        text: 'Registration Start Date',
      },
      registrationEndDate: {
        rules: 'required',
        text: 'Registration End Date',
      },
      earlyBirdDiscount: {},
      discountRate: {},
      quota: {},
      downPayment: {},
    },
  ],
  validations: [
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
  ],
  getRouteIndex(route) {
    for (let i = 0; i < routes.length; i++) {
      if (routes[i].name === (route || store.state.createCourseVm.$route).name) {
        return i
      }
    }
  },
  goPrevPage() {
    const vm = store.state.createCourseVm
    vm.$router.push(routes[this.getRouteIndex() - 1])
  },
  goNextPage() {
    const vm = store.state.createCourseVm
    vm.$router.push(routes[this.getRouteIndex() + 1])
  },
  checkAndGoNextPage(alert = true) {
    return this.checkIsValidCurrentPage().then(() => {
      this.goNextPage()
    }, (e) => {
      // invalid
      if (alert) {
        const validation = this.validations[this.getRouteIndex()]
        Vue.alert(validation.getFirstError().message)
      } else {
        throw e
      }
    })
  },
  async checkIsValidByIndex(index) {
    const fields = this.fields[index]
    const validation = this.validations[index]
    if (validation.isPause || !validation.check) {
      // pause or not init validate
      const vm = store.state.appVm
      vm.$validate(validation, fields)
      // wait 10 ms
      await new Promise(function(resolve, reject) {
        setTimeout(function () {
          resolve()
        }, 10);
      });
    }
    return validation.check()
  },
  async checkIsValidTillIndex(index) {
    for (let i = 0; i <= index; i++) {
      await this.checkIsValidByIndex(i).catch(e => {
        e.index = i
        throw e
      })
    }
  },
  checkIsValidCurrentPage() {
    const index = this.getRouteIndex()
    return this.checkIsValidByIndex(index)
  },
  submitting: false,
  submit() {
    const vm = store.state.appVm
    if (this.submitting) {
      return
    }
    this.submitting = true
    this.checkIsValidTillIndex(this.fields.length - 1).then(() => {
      const data = {
        accomodation_detail: {},
      }
      this.validations.forEach((vl, i) => {
        if (i !== 0) {
          const {fields} = vl
          const values = {}
          // process value
          for (var key0 in fields) {
            const key = snakeCase(key0)
            const fld = fields[key0]
            if (key.endsWith('date')) {
              values[key] = parseInt(newDate(fld.value).getTime() / 1000)
            } else {
              values[key] = fld.type === 'json' ? JSON.stringify(fld.value) : fld.value
            }
          }
          //
          if (i === 8) {
            Object.assign(data.accomodation_detail, values)
          } else {
            Object.assign(data, values)
          }
        }
      })
      return vm.$http.post(`${vm.$state.urls.api}/course_detail`, data).then(({data}) => {
        vm.$alert(`Saved Successfully`)
      }, (e) => {
        console.log(e);
        vm.$alert(`Save Failed. ${e.response.data.message || ''}`)
      })
    }, e => {
      if (e.index != null) {
        const invalidRoute = this.routes[e.index]
        vm.$router.push(invalidRoute)
      }
    }).then(() => {
      this.submitting = false
    })
  },
}
export default state
