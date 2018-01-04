import store from './index'
import {createCourse as routes} from '@/routes/index'

export default {
  fields: {
    start: {
      declared: {
        rules: 'required|accepted',
      },
      agreed: {
        rules: 'required|accepted',
      },
    },
    step1: {
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
  },
  validations: {
    start: {},
    step1: {},
  },
  pageOrder: ['start', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'step8', 'step9'],
  getRouteIndex() {
    for (let i = 0; i < routes.length; i++) {
      if (routes[i].name === store.state.createCourseVm.$route.name) {
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
  checkIsValidByKey(key) {
    const fields = this.fields[key]
    const validation = this.validations[key]
    if (validation.isPause) {
      // pause or not init validate
      const vm = store.state.createCourseVm
      vm.$validate(validation, fields)
    }
    return validation.check()
  },
  async checkIsValidTillKey(key) {
    for (const key2 of this.pageOrder) {
      await this.checkIsValidByKey(key2)
      if (key2 === key) {
        break
      }
    }
  },
  checkIsValidCurrentPage() {
    const index = this.getRouteIndex()
    let key
    if (index === 0) {
      key = 'start'
    } else {
      key = `step${index}`
    }
    return this.checkIsValidByKey(key)
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
