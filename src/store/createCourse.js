import Vue from 'vue'
import store from './index'
import {createCourse as routes} from '@/routes/index'

export default {
  routes,
  ignoreValidation: true, // only when developing
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
    step2: {
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
    step3: {
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
    step4: {
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
    step5: {
      provide: {
        rules: '',
        text: 'What You’ll Provide?',
      },
      guestNeedsToBring: {
        rules: '',
        text: 'What Your Guest Needs to Bring?',
      },
    },
    step6: {
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
    step7: {
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
    step8: {},
    step9: {},
  },
  validations: {
    start: {},
    step1: {},
    step2: {},
    step3: {},
    step4: {},
    step5: {},
    step6: {},
    step7: {},
    step8: {},
    step9: {},
  },
  pageOrder: ['start', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'step8', 'step9'],
  getRouteIndex(route) {
    for (let i = 0; i < routes.length; i++) {
      if (routes[i].name === (route || store.state.createCourseVm.$route).name) {
        return i
      }
    }
  },
  getPageName(route) {
    const index = this.getRouteIndex(route)
    return this.pageOrder[index]
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
        const validation = this.validations[this.getPageName()]
        Vue.alert(validation.getFirstError().message)
      } else {
        throw e
      }
    })
  },
  async checkIsValidByKey(key) {
    const fields = this.fields[key]
    const validation = this.validations[key]
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
  async checkIsValidTillKey(key) {
    for (let i = 0; i < this.pageOrder.length; i++) {
      const key2 = this.pageOrder[i]
      await this.checkIsValidByKey(key2).catch(e => {
        e.index = i
        throw e
      })
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
