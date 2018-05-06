<template lang="pug">
CardContainer.create-program
  .page0.text-center(v-if="page===0")
    .title I want to create
    ._1
      b.text-box(:class="{active:withAccom}" @click="withAccom=true") A Program<br>"With" Accomodation <QuestionCircle/>
      .or OR
      b.text-box(:class="{active:!withAccom}" @click="withAccom=false") A Program<br>"Without" Accomodation <QuestionCircle/></span>
    ._2
      el-checkbox(v-model="pages[0].agreed")
      span.mls I acknowledge that Borocol will take service charge (13%) on per succesful application. I hereby agree to “<a><b>Terms of Service</b></a>” and understanding the purpose of collecting personal data.
    .mtl
    el-button.confirm-btn(type="primary" size="large" @click="page0confirm") Confirm
  div(v-else :class="'page' + page")
    .cp-header
      .step Step {{stepText}}
      .title {{pageCur.title}}
    el-progress(:text-inside='true', :stroke-width='20', :percentage="progress", color="#fc0")
    .cp-body
      el-row(:gutter="80")
        //- left
        el-col.mbm(:sm="15" :md="16" :lg="17")
          //- page 1
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
                FormItem(:field="pageCur.fields.categoryId" type="select" :options="[{value: 1, text: 'todo'}]")
              el-col.mbm(:md="9")
                FormItem(:field="pageCur.fields.level" type="select" :options="[{value: 1, text: 'todo'}]")
              el-col.mtl.hidden-sm-and-down
              el-col.mbm(:md="25")
                FormItem(:field="pageCur.fields.title")
          //- page 2
          div(v-else-if="page===2")
            el-row(:gutter="24")
              el-col.mbm(:md="8")
                FormItem(:field="pageCur.fields.gender")
                  GenderSelect(slot="control" v-model="pageCur.fields.gender.value")
              el-col.mbm(:md="16")
                FormItem(:field="pageCur.fields.ageRange")
                  el-slider(slot="control" range :min="16" :max='100'
                    v-model="pageCur.fields.ageRange.value"
                  )
              el-col.mtl.hidden-sm-and-down
              el-col.mbm
                FormLabel(:field="pageCur.fields.hours")
                .time-range.mlm
                  el-input(v-model.number="pageCur.fields.hours.value[0]" type="number")
                  .divider -
                  el-input(v-model.number="pageCur.fields.hours.value[1]" type="number")
              el-col.mtl.hidden-sm-and-down
              el-col.mbm
                FormItem(:field="pageCur.fields.description" type="textarea"
                  :controlAttrs="{rows:8}"
                )
          //- page 3
          div(v-else-if="page===3")
            FormLabel Introduce the host/ instructor to your guests.
            .mtm
              el-checkbox(v-model="pageCur.autoFill")
              span.mls I am the Host/ Instructor, please auto fill in details from my profile.
            .mbm
            h2 Main
            .mbm
            .instructor-layout
              .instructor-layout-inputs
                el-row(:gutter="16")
                  el-col.mbm(:sm="12")
                    .form-item
                      FormLabel Name
                      el-input(v-model="pageCur.fields.instructors.value[0].name" placeholder="Full Name")
                  el-col.mbm(:sm="12")
                    .form-item
                      FormLabel Contact Number
                      PhoneInput(v-model="pageCur.fields.instructors.value[0].phone")
                  el-col.mbm
                    el-input(type="textarea" :rows="3" v-model="pageCur.fields.instructors.value[0].description"
                      placeholder="e.g., Selena has 10 years experiene in teaching diving skills...."
                    )
              .instructor-layout-photo
                ImageUploader(v-model="pageCur.fields.instructors.value[0].photo")
            .mbm
            h2 Second
            .mbm
            .instructor-layout
              .instructor-layout-inputs
                el-row(:gutter="16")
                  el-col.mbm(:sm="12")
                    .form-item
                      FormLabel Name
                      el-input(v-model="pageCur.fields.instructors.value[1].name" placeholder="Full Name")
                  el-col.mbm(:sm="12")
                    .form-item
                      FormLabel Contact Number
                      PhoneInput(v-model="pageCur.fields.instructors.value[1].phone")
                  el-col.mbm
                    el-input(type="textarea" :rows="3" v-model="pageCur.fields.instructors.value[1].description"
                      placeholder="e.g., Selena has 10 years experiene in teaching diving skills...."
                    )
              .instructor-layout-photo
                ImageUploader(v-model="pageCur.fields.instructors.value[1].photo")
            .mbm
            FormItemInline(:field="pageCur.fields.language" placeholder="English, Spanish")
          //- page 4
          div(v-else-if="page===4")
            .mbm
              FormLabel(required) Fill in the address
            .address-area
              .mbm
                FormItemInline(:field="pageCur.fields.street")
              el-row(:gutter="16")
                el-col.mbm(:md="8")
                  FormItemInline(:field="pageCur.fields.city")
                el-col.mbm(:md="16")
                  FormItemInline(:field="pageCur.fields.province")
                el-col.mbm(:md="8")
                  FormItemInline(:field="pageCur.fields.zipCode")
                el-col.mbm(:md="8")
                  FormItemInline(:field="pageCur.fields.country")
                    NationSelect(slot="control" v-model="pageCur.fields.country.value")
                el-col.mbm(:md="8")
                  el-input.api-key(v-model="pageCur.fields.apiKey.value")
                    img.api-key-img(src="~assets/img/google-map.png" slot="prepend")
            FormItem.mbm(:field="pageCur.fields.locationDescription" type="textarea" :controlAttrs="{rows:3}")
            el-row(:gutter="16")
              el-col.mbm(:md="12")
                FormItem.mbm(:field="pageCur.fields.howToGetThere" type="textarea"
                  :controlAttrs="{rows:5}"
                  placeholder="e.g., Please book your flight to arrive at JFK Airport, New York."
                )
              el-col.mbm(:md="12")
                FormItem.mbm(:field="pageCur.fields.whereToMeet" type="textarea"
                  :controlAttrs="{rows:5}"
                  placeholder="e.g., (This is an “Auto Message”) We will meet up at Plaza Hotel’s Reception at 2:00 p.m. on Jul 8, 2017."
                )
          //- page 5
          div(v-else-if="page===5")
            FormItem.mbm(:field="pageCur.fields.schedule" type="textarea"
              :controlAttrs="{rows:6}"
              placeholder="Day1\nDay2\nDay3"
            )
            FormItemInline.mbm(:field="pageCur.fields.mealsIncluded")
              el-radio-group(slot="control" v-model="pageCur.fields.mealsIncluded.value")
                el-radio(:label="false") No
                el-radio(:label="true") Yes
            el-checkbox-group.mbm(v-model="pageCur.fields.meals.value")
              el-checkbox(label="breakfast") Breakfast
              el-checkbox(label="lunch") Lunch
              el-checkbox(label="bunch") Bunch
              el-checkbox(label="dinner") Dinner
              el-checkbox(label="snacks") Snacks
            FormItem(:field="pageCur.fields.weatherArrangement" type="textarea"
              :controlAttrs="{rows: 5}"
            )
          //- page 6
          div(v-else-if="page===6")
            FormItem.mbm(:field="pageCur.fields.provide" type="textarea"
              :controlAttrs="{rows:6}"
              placeholder="- Equipment\n- Airport Pickup\n- Towels"
            )
            FormItem.mbm(:field="pageCur.fields.guestNeedsToBring" type="textarea"
              :controlAttrs="{rows:6}"
              placeholder="- Goggle\n- Swimsuits"
            )
            FormItemInline.mbm(:field="pageCur.fields.issueCertificate" break-line)
              el-radio-group(slot="control" v-model="pageCur.fields.issueCertificate.value")
                el-radio(:label="false") No
                el-radio(:label="true") Yes
            el-input(v-model="pageCur.fields.certificate.value" type="textarea"
              :rows="5" placeholder="With at least 70% attendance..."
            )
          //- page 7
          div(v-else-if="page===7")
            FormItem.mbm(:field="pageCur.fields.entryRequirment" type="textarea"
              :controlAttrs="{rows:5}"
              placeholder="- Skill level\n- Occupations"
            )
            FormItemInline.mbm(:field="pageCur.fields.requestFormEnabled" break-line)
              el-radio-group(slot="control" v-model="pageCur.fields.requestFormEnabled.value")
                el-radio(:label="false") No
                el-radio(:label="true") Yes
            .request-form
              .request-form-item.mbm
                el-checkbox(v-model="pageCur.fields.requestForm.value[0].enabled")
                span.rf1 Question 1:
                el-input(v-model="pageCur.fields.requestForm.value[0].value"
                  type="textarea" :rows="2"
                )
              .request-form-item.mbm
                el-checkbox(v-model="pageCur.fields.requestForm.value[1].enabled")
                span.rf1 Question 2:
                el-input(v-model="pageCur.fields.requestForm.value[1].value"
                  type="textarea" :rows="2"
                )
          //- page 8
          div(v-else-if="page===8")
            FormItemInline.mbm(:field="pageCur.fields.type" break-line)
              el-select.inline-input(slot="control" v-model="pageCur.fields.type.value")
                el-option(v-for="item in pageCur.fields.type.options"
                  :key="item.text"
                  :label="item.text"
                  :value="item.value"
                )
            el-row(:gutter="16")
              el-col.mbm(:md="12")
                FormItemInline(:field="pageCur.fields.name")
              el-col.mbm(:md="12")
                FormItemInline(:field="pageCur.fields.tel")
                  PhoneInput(slot="control" v-model="pageCur.fields.tel.value")
            FormItemInline.mbm(:field="pageCur.fields.address")
            FormItem.mbm(:field="pageCur.fields.facilities")
              el-checkbox-group(slot="control" v-model="pageCur.fields.facilities.value")
                el-checkbox(label="wifi") Wifi
                el-checkbox(label="gym") Gym
                el-checkbox(label="air-conditionor") Air-conditionor
                el-checkbox(label="heater") Heater
                el-checkbox(label="balcony") Balcony
                el-checkbox(label="free parking") Free parking
                el-checkbox(label="washing machine") Washing machine
                el-checkbox(label="drying machine") Drying Machine
                el-checkbox(label="swimming pool") Swimming pool
                el-checkbox(label="kitchen") Kitchen
            FormItem.mbm(:field="pageCur.fields.description" type="textarea" :controlAttrs="{rows:3}"
              placeholder="ABC Resorts is located at Country side…."
            )
            FormItemInline.mbm(:field="pageCur.fields.photos")
              MultipleImageUploader(slot="control" v-model="pageCur.fields.photos.value" :boxSpace="16")
          //- page 9
          div(v-else-if="page===9")
            .group-size-seat-price
              FormItemInline.mbm(:field="pageCur.fields.groupSize")
              FormItemInline.mbm(:field="pageCur.fields.seatQuota")
              FormItemInline.mbm(v-if="!withAccom" :field="pageCur.fields.price" placeholder="USD")
            FormItem(v-if="withAccom" :field="pageCur.fields.rooms")
              el-row.rooms.mtm(slot="control" :gutter="16")
                template(v-for="(item, i) in rooms")
                  el-col.mbm(:sm="12" :lg="8")
                    el-checkbox.mrm(v-model="item.enabled")
                    el-select(v-model="item.type")
                      el-option(v-for="v in roomTypes" :key="v.text"
                        :value="v.value"
                      ) {{v.text}}
                  el-col.mbm(:sm="12")
                    span.mrs Quota
                    el-input.mrm.quota-input(v-model="item.quota")
                    span.mrs Price
                    el-input.price-input.mrl(v-model="item.price" placeholder="USD")
                    el-button(type="danger" icon="el-icon-delete" circle @click="rooms.splice(i, 1)")
                el-col.mbm()
                  el-button(icon="el-icon-plus" type="primary" circle @click="addRoom")
          //- page 10 Additional Options
          div(v-else-if="page===10")
            h2.mbl Additional Options
            el-row(type="flex")
              el-checkbox(v-model="earlyBird.enabled")
              .checkbox-right.mlm
                FormLabel I’d like to offer “<b class="yellow">Early Bird</b>” discount.
                el-row(:gutter="16")
                  el-col.mbm(:sm="12")
                    el-row(type="flex" align="middle")
                      span.mrs Discount Rate
                      el-select.discount-select(v-model="earlyBird.discount")
                        el-option(:value="0.1") 10% off
                        el-option(:value="0.2") 20% off
                        el-option(:value="0.3") 30% off
                        el-option(:value="0.4") 40% off
                        el-option(:value="0.5") 50% off
                  el-col.mbm(:sm="12")
                    el-row(type="flex" align="middle")
                      span.mrs Quota
                      el-input.quota-input(v-model="earlyBird.quota")
            el-row.mtm(type="flex")
              el-checkbox(v-model="downPayment.enabled")
              .checkbox-right.mlm
                FormLabel I’d like to provide “<b class="primary">Down Payment</b>” option.
                div
                  span.mrs Down Payment Rate
                  el-select.discount-select(v-model="downPayment.discount")
                    el-option(:value="0.1") 10% off
                    el-option(:value="0.2") 20% off
                    el-option(:value="0.3") 30% off
                    el-option(:value="0.4") 40% off
                    el-option(:value="0.5") 50% off
                  .mtm
                    .mbm How would you like your guest to pay the rest of the fee?
                    el-input(type="textarea" :rows="3"
                      v-model="downPayment.rest"
                      placeholder="Please have your check or cash ready on the arrival day."
                    )
                  FormItemInline.mtm(break-line)
                    FormLabel(slot="label") Registration End Day
                    el-date-picker.date-picker1(slot="control" type="date" v-model="earlyBird.endDate")
          //- page 11
          div(v-else-if="page===11")
            FormLabel Upload photos of your program (Min. 3)
            .cover-photos.mts
              .mrl
                .text-center Cover Photo
                ImageUploader(v-model="pageCur.fields.cover.value")
              div
                div &nbsp;
                MultipleImageUploader(v-model="pageCur.fields.photos.value" :boxSpace="16")
            FormItem.mtl(:field="pageCur.fields.youtubeVideoLink")
            FormItem.mtl(:field="pageCur.fields.tags")
              el-select(slot="control" v-model="pageCur.fields.tags.value"
                multiple filterable allow-create default-first-option
                placeholder="Input or select tag"
              )
                el-option(v-for="item in hotTags" :key='item' :value="item") {{item}}
        //- right
        el-col(:sm="9" :md="8" :lg="7")
          .cp-tips
            .tip
              .tip-title
                Icon(name="idea")
                | Tips
              .tip-text {{pageCur.tips && pageCur.tips[0] || 'More information more chance to attract your student!'}}
            .tip
              .tip-title
                Icon(name="idea")
                | Tips
              .tip-text(v-if="page===9")
                b.teal How to deal with the odd number situation?
                p You will never know how many guest will be participating in your program, For the odd number, we suggest our host to reserve an extra bedroom to solve this problem.
              .tip-text(v-else) {{pageCur.tips && pageCur.tips[1] || 'More information more chance to attract your student!'}}
          .cp-actions
            a.cp-action(@click="page--") Back
            a.cp-action.cp-action-next(v-if="page < 11" @click="next")
              Icon(name="arrow-right")
            a.cp-action.cp-action-next.primary(v-else @click="preview")
              | Preview
</template>

<script>
import CardContainer from '@/components/CardContainer'
import ImageUploader from '@/components/ImageUploader';
import MultipleImageUploader from '@/components/MultipleImageUploader';
import NationSelect from '@/components/NationSelect';
import GenderSelect from '@/components/GenderSelect';
import PhoneInput from '@/components/PhoneInput';
import FormItemInline from '@/components/FormItemInline';
import * as hp from 'helper-js'
import * as ut from '@/plugins/utils'

export default {
  middleware: ['auth', 'isSchool'],
  components: {CardContainer, ImageUploader, MultipleImageUploader,
    NationSelect, GenderSelect, PhoneInput, FormItemInline},
  data() {
    const {siteName} = this.$store.state
    return {
      loading: false,
      withAccom: true,
      page: 8,
      pages: [
        {
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
          step: 1,
          title: 'Start with the basic 1.2',
          fields: {
            gender: {text: 'Gender', rules: 'required'},
            ageRange: {text: 'Age', value: [16, 32]},
            hours: {text: 'How many hour will It take to complete this program?',
              rules: 'required|hours', value:[null, null],
              customRules: {
                hours({value}) {
                  return value.every(v => v != null && hp.isNumber(v))
                },
              },
              messages: {
                hours({value, field}) {
                  for (const v of value) {
                    if (v == null) {
                      return `The ${field.name} is required`
                    } else if (!hp.isNumber(v)) {
                      return `The ${field.name} must be number`
                    }
                  }
                },
              },
            },
            description: {text: 'Description of the program (What we will do)', nameInMessage: 'description', rules: 'required'},
          },
        },
        // 3
        {
          step: 1,
          autoFill: false,
          title: 'Start with the basic 1.3',
          tips:['If the host is a different person from the one who registered this account, please tick “Main” or “Second” to fill in profile.',
            'Contact number will only be shown on the confirmation page once the guest successfully book the program.',
          ],
          fields: {
            language: {text: 'This Program Will be Offered in', nameInMessage: 'language', rules: 'required'},
            instructors: {
              value: [
                {name: null, phone: null, description: null, photo: null},
                {name: null, phone: null, description: null, photo: null},
              ],
            },
          },
        },
        {
          step: 1,
          title: 'Start with the basic 1.4',
          tips:['How to insert API Key',
            'More information more chance to attract your student!',
          ],
          fields: {
            street: {
              rules: 'required',
              text: 'Street',
            },
            city: {
              rules: 'required',
              text: 'City',
            },
            province: {
              rules: 'required',
              text: 'State/ Province/ Region',
              nameInMessage: 'province',
            },
            zipCode: {
              rules: 'required',
              text: 'Zip Code',
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
              rules: 'required',
              text: 'Describe the location/ venue',
            },
            howToGetThere: {
              rules: 'required',
              text: 'How to get there?',
            },
            whereToMeet: {
              rules: 'required',
              text: 'Where to meet up your guest?',
            },
          },
        },
        {
          step: 2,
          title: 'General Details 2.1',
          fields: {
            schedule: {
              rules: 'required',
              text: 'Tell your guests the itinerary / daily schedule',
              nameInMessage: 'schedule',
            },
            mealsIncluded: {
              text: 'Are meals included?',
              value: true,
            },
            meals: {
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: ({fields}) => fields.mealsIncluded.value
              },
              value: [],
            },
            weatherArrangement: {
              text: 'Is there any bad weather arrangement?',
            },
          },
        },
        {
          step: 2,
          title: 'General Details 2.2',
          fields: {
            provide: {
              rules: '',
              text: 'What You’ll Provide?',
            },
            guestNeedsToBring: {
              rules: '',
              text: 'What Your Guest Needs to Bring?',
            },
            issueCertificate: {
              value: true,
              text: 'Will you issue certificate to your guests?',
            },
            certificate: {
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: ({fields}) => fields.issueCertificate.value
              },
            },
          },
        },
        {
          step: 2,
          title: 'General Details 2.3',
          fields: {
            entryRequirment: {
              text: 'Is there any entry requirment?',
            },
            requestFormEnabled: {
              text: 'Would you like to set up a request form?',
            },
            // need validate in server
            requestForm: {
              rules: '',
              value: [{enabled: false, value: null}, {enabled: false, value: null}],
            },
          },
        },
        // Accomodation 8
        {
          step: 3,
          title: 'Accomodation',
          fields: {
            type: {
              text: 'Select the type of accomodation you provide',
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: () => this.withAccom
              },
              nameInMessage: 'accomodation type',
              value: 'hotel',
              options: [
                {value: 'hotel', text: 'Hotel'},
              ],
            },
            name: {
              text: 'Name',
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: () => this.withAccom
              },
              nameInMessage: 'accomodation name',
            },
            tel: {
              text: 'Tel',
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: () => this.withAccom
              },
              nameInMessage: 'accomodation tel',
            },
            address: {
              text: 'Address',
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: () => this.withAccom
              },
              nameInMessage: 'accomodation address',
            },
            facilities: {
              text: 'What facilities do they offer?',
              value: [],
            },
            description: {
              text: 'Description',
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: () => this.withAccom
              },
              nameInMessage: 'accomodation description',
            },
            photos: {
              text: 'Upload photos',
              value: [],
            },
          },
        },
        // 9
        // below step is dynamic
        {
          step: 4,
          title: 'Pricing & Quota',
          tips: [`Please make sure you have enough seat for people to register through our platform (${siteName}).`],
          fields: {
            groupSize: {
              rules: 'required|integer',
              text: 'How many guest in total will be participating in this program? (Group Size)',
              nameInMessage: 'group size',
            },
            seatQuota: {
              rules: 'required|integer',
              text: `How many seat will be available for guest to register on ${siteName}?`,
              nameInMessage: 'seat quota',
            },
            price: {
              rules: 'requiredIf|integer',
              ruleParams: {
                requiredIf: () => !this.withAccom
              },
              text: 'How much do you charge per guest? (Price)',
              nameInMessage: 'price',
            },
            rooms: {
              rules: 'requiredIf',
              ruleParams: {
                requiredIf: () => this.withAccom
              },
              text: 'Please select room type, price & quota: ',
              value: [
                {enabled: false, type: 'shared half', quota: null, price: null},
                {enabled: false, type: 'shared 3 ppl', quota: null, price: null},
                {enabled: false, type: 'private double bed', quota: null, price: null},
              ],
            },
          },
        },
        // 10
        // 4/5 Additional Options
        {
          step: 5,
          title: 'Pricing & Quota',
          fields: {
            // need validate in server
            earlyBird: {
              value: {enabled: false, discount: null, quota: null, endDate: null},
            },
            downPayment: {
              value: {enabled: false, discount: null, rest: null},
            },
          },
        },
        // 11
        // 5/6 Make your Program Looks more Attractive
        {
          step: 6,
          title: 'Pricing & Quota',
          fields: {
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
            youtubeVideoLink: {
              text: 'Insert a “Youtube” video link',
            },
            tags: {
              rules: '',
              text: 'Tags',
              value: [],
            },
          },
        },
      ],
      roomTypes: [
        {value: 'shared half' ,text: 'Shared Room(Half)'},
        {value: 'shared 3 ppl' ,text: 'Shared Room (3 ppl)'},
        {value: 'private double bed' ,text: 'Private Room (Double Bed)'},
      ],
      // todo get from server
      hotTags: ['Design', 'IT'],
    }
  },
  computed: {
    pageCur() { return this.pages[this.page] },
    stepText() {
      let {step} = this.pageCur
      if (this.page > 8) {
        return this.withAccom ? step : (step - 1)
      }
      return step
    },
    progress() {
      let {page} = this
      let len = this.pages.length - 1
      if (page > 8 && !this.withAccom) {
        page--
        len--
      }
      return Math.floor(page / len * 100)
    },
    // raise
    rooms() { return this.pages[9].fields.rooms.value },
    earlyBird() { return this.pages[10].fields.earlyBird.value },
    downPayment() { return this.pages[10].fields.downPayment.value },
  },
  watch: {
    'pages.3.autoFill': {
      immediate: true,
      async handler(autoFill) {
        if (autoFill) {
          const {data} = await this.$apiPost('/user/profile')
          const instructor = this.pages[3].fields.instructors.value[0]
          Object.assign(instructor, {
            name: `${data.firstName} ${data.lastName}`,
            phone: data.phone,
            photo: data.avatar
          })
        }
      }
    }
  },
  methods: {
    page0confirm() {
      if (!this.pages[0].agreed) {
        this.$alert('Please accept the terms.')
      } else {
        this.page++
      }
    },
    async next() {
      if (this.pageCur.validation) {
        await this.$checkValidation(this.pageCur.validation)
      }
      this.page++
    },
    async preview () {
      // todo
      const data = {withAccom: this.withAccom}
      this.pages.forEach((page, i) => {
        if (i === 8) {
          return
        }
        Object.keys(page.fields).forEach(key => {
          data[key] = page.fields[key].value
        })
      })
      const p9 = this.pages[9]
      data.accomodation = {rooms: p9.fields.rooms.value}
      const p8 = this.pages[8]
      Object.keys(p8.fields).forEach(key => {
        data.accomodation[key] = p8.fields[key].value
      })
      this.loading = true
      await this.$apiPost('/course', data)
      this.$alert(`Created Successfully`, '')
      this.loading = false
    },
    addRoom() {
      this.rooms.push({enabled: false, type: null, quota: null, price: null})
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
    margin-left: 30px;
  }
  @media(max-width: $medium) {
    height: auto;
    line-height: 50px;
    font-size: 18px;
    .step{
      width: 80px;
    }
    .title{
      margin-left: 5px;
    }
  }
}
.cp-body{
  padding: 50px 100px;
  @media(max-width: $medium) {
    padding: 20px;
  }
}
.cp-tips{
  .tip{
    border-width: 2px;
    border-color: #ddd;
    border-style: solid;
    border-radius: 3px;
    padding: 15px 20px;
    margin-bottom: 30px;
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
    font-size: 13px;
    font-weight: 500;
  }
  @media(max-width: $medium) {
    .tip{
      padding: 5px 10px;
      border-width: 1px;
      margin-bottom: 10px;
    }
    .tip-title{
      font-size: 18px;
      .icon{
        font-size: 20px;
        margin-right: 10px;
      }
    }
    .tip-text{
      margin-top: 5px;
    }
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
.quota-input{
  width: 100px;
  display: inline-block;
}
.price-input{
  width: 120px;
  display: inline-block;
}
.discount-select{
  width: 150px;
  display: inline-block;
}
.date-picker1{
  max-width: 200px;
}
.primary{
  color: $primaryColor;
}
.yellow{
  color: #ffcc00;
}
.teal{
  color: teal;
}
//
.page0{
  padding: 100px 10px;
  @media(max-width: $medium) {
    padding: 50px 10px;
  }
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
.page3{}
.instructor-layout{
  display: flex;
}
.instructor-layout-photo{
  margin-left: 40px;
  flex-shrink: 0;
}
@media(max-width: $medium) {
  .instructor-layout{
    display: block;
  }
  .instructor-layout-photo{
    margin-left: 0;
  }
}
.page4{}
.address-area{
  .form-label{
    font-weight: 400;
  }
  .required-asterisk{
    display: none;
  }
}
.api-key{
  .el-input-group__prepend{
    padding: 0;
  }
  .api-key-img{
    float: left;
  }
}
.page7{}
.request-form-item{
  display: flex;
  align-items: center;
}
.rf1{
  margin-left: 1em;
  margin-right: 2em;
  flex-shrink: 0;
}
@media(max-width: $small) {
  .request-form-item{
    display: block;
  }
  .request-form{
    .el-textarea{
      margin-top: .5em;
    }
  }
}
.page9{}
.group-size-seat-price{
  .fii-label{
    flex-shrink: 1;
  }
  .fii-control{
    text-align: right;
  }
  .el-input{
    width: 70px;
  }
}
.rooms{
  .el-col{
    display: flex;
    align-items: center;
  }
}
.page10{}
.checkbox-right{
  flex-grow: 1;
}
.page11{}
.cover-photos{
  display: flex;
  flex-wrap: wrap;
}
</style>
