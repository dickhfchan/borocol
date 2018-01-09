import Vue from 'vue'
import store from './index'
import {createCourse as routes} from '@/routes/index'

export const steps = [
  {index: 1, pageRange: [1,2], title: 'Start with the basic'},
  {index: 2, pageRange: [3, 3], title: 'Location'},
  {index: 3, pageRange: [4, 5], title: 'General Details'},
  {index: 4, pageRange: [6, 6], title: 'Request Form'},
  {index: 5, pageRange: [7, 7], title: 'Make your program looks more attractive'},
  {index: 6, pageRange: [8, 8], title: 'Accomodation'},
  {index: 7, pageRange: [9, 9], title: 'Accomodation Pricing & Quota'},
  {index: 8, pageRange: [10, 10], title: 'Pricing & Quota'},
]
export default {
  routes,
  ignoreValidation: true, // only when developing
  steps,
  fields: [
    {
      declared: {
        rules: 'required|accepted',
      },
      agreed: {
        rules: 'required|accepted',
      },
    },
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
      },
    },
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
    {},
    {},
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
  formData: {
    declared: false,
    agreed: false,
    // 1
    title: null,
    category: null,
    level: null,
    startDate: null,
    endDate: null,
    description: null,
    // 2
    groupSize: null,
    gender: null,
    ageRange: [16, 30],
    hours: null,
    language: null,
    instructorPhoto: null,
    instructorInfo: null,
    issueCertificate: null,
    certification: null,
    // 3
    address: null,
    // 4
    mealsIncluded: null,
    meals: null,
  },
  formDataMapping: {
    // 1
    title: 'name',
    // 2
    // groupSize
    // gender
    // hours
    // instructorPhoto,
    // instructorInfo,
    issueCertificate: 'certification',
    certification: 'certification_name',
    // 3
    // address
    // city
    // apiKey
    // locationDescription
    // howToGetThere
    // whereToMeetUpYourGuest
    // 4
    // schedule
    // mealsIncluded
    // meals
    // mealsInfo
    // 5

  },
}
