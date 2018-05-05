<template lang="pug">
CardContainer.student-profile
  .pal
    .card-container-title Profile
    form.mtl(@submit.prevent="save")
      el-row(:gutter="16")
        el-col(:md="18")
          ._1
            ImageUploader.avatar-uploader.mrl(:aspectRatio="1/1" v-model="fields.avatar.value" title="Upload Photo")
            el-row._1r(:gutter="16")
              el-col(:span="24")
                .form-item
                  .form-label
                    span.required-asterisk *
                    span  Name on Passport
              el-col.mbm(:sm="8")
                FormItem(:field="fields.firstName")
                  el-input(v-model="fields.firstName.value" placeholder="* First Name")
                  FormError(:field="fields.firstName")
              el-col.mbm(:sm="8")
                FormItem(:field="fields.middleName")
                  el-input(v-model="fields.middleName.value" placeholder="Middle Name")
                  FormError(:field="fields.middleName")
              el-col.mbm(:sm="8")
                FormItem(:field="fields.lastName")
                  el-input(v-model="fields.lastName.value" placeholder="* Last Name")
                  FormError(:field="fields.lastName")
              el-col.mbm(:sm="8")
                FormItem(:field="fields.gender")
                  GenderSelect(slot="control" v-model="fields.gender.value")
              el-col.mbm(:sm="8")
                FormItem(:field="fields.birthday")
                  el-date-picker(slot="control" type="date"
                    v-model="fields.birthday.value"
                  )
              el-col.mbm(:sm="8")
                FormItem(:field="fields.nationality")
                  NationSelect(slot="control" v-model="fields.nationality.value")
          el-row.mtm(:gutter="16")
            el-col.mbm(:sm="7")
              FormItem(:field="fields.countryOfResidence")
                NationSelect(slot="control" v-model="fields.countryOfResidence.value")
            el-col.mbm(:sm="10")
              FormItem(:field="fields.email")
            el-col.mbm(:sm="7")
              FormItem(:field="fields.phone")
                PhoneInput(slot="control" v-model="fields.phone.value")
            el-col(:span="24")
              .form-item
                .form-label
                  span.required-asterisk *
                  span Passport Information
            el-col.mbm(:sm="8")
              el-input(v-model="passportInfo.number" placeholder="Passport Number")
            el-col.mbm(:sm="8")
              NationSelect(v-model="passportInfo.issuedCountry" placeholder="Issued Country")
            el-col.mbm(:sm="8")
              el-date-picker(
                v-model="passportInfo.expiryDate"
                type="date" placeholder="Expiry Date"
              )
        el-col(:md="6")
          el-row(:gutter="16")
            el-col(:span="24")
              .form-item
                .form-label
                  span.required-asterisk *
                  span Emergency Contact Person 1
            el-col.mbm
              el-input(v-model="ecp[0].name" placeholder="Name")
            el-col.mbm(:sm="12")
              el-input(v-model="ecp[0].relationship" placeholder="Relationship")
            el-col.mbm(:sm="12")
              el-input(v-model="ecp[0].tel" placeholder="Tel")
            //- 2
            el-col(:span="24")
              .form-item
                .form-label
                  span Emergency Contact Person 2
            el-col.mbm
              el-input(v-model="ecp[1].name" placeholder="Name")
            el-col.mbm(:sm="12")
              el-input(v-model="ecp[1].relationship" placeholder="Relationship")
            el-col.mbm(:sm="12")
              el-input(v-model="ecp[1].tel" placeholder="Tel")
          .declare
            el-checkbox(v-model="fields.declared.value")
            .mlm
              p I hereby declare that all information provided above is true and accurate.
              p.mtm I agree to <a href="#"><b>Borocol’s Terms of Service</b></a> and undestating <a href="#"><b>the purpose of collecting personal data</b></a>.
          .mtm
            el-button.btn-block(native-type="submit" type="primary" size="large") Save
</template>

<script>
import CardContainer from '@/components/CardContainer'
import ImageUploader from '@/components/ImageUploader';
import NationSelect from '@/components/NationSelect';
import GenderSelect from '@/components/GenderSelect';
import PhoneInput from '@/components/PhoneInput';
import * as hp from 'helper-js'
import * as ut from '@/plugins/utils'

export default {
  components: {CardContainer, ImageUploader, NationSelect, GenderSelect, PhoneInput},
  props: ['data'],
  data() {
    return {
      fields: {
        avatar: {
          rules: 'required',
          type: 'file',
        },
        firstName: {
          rules: 'required',
          text: 'First Name',
        },
        middleName: {
        },
        lastName: {
          rules: 'required',
          text: 'Last Name',
        },
        gender: {
          rules: 'required',
          text: 'Gender',
        },
        birthday: {
          rules: 'required',
          type: 'date',
          text: 'Birthday',
        },
        nationality: {
          rules: 'required',
          text: 'Nationality',
        },
        countryOfResidence: {
          rules: 'required',
          text: 'Country of Residence'
        },
        email: {
          rules: 'required|email',
          text: 'Email',
        },
        phone: {
          rules: 'required|phone',
          text: 'Phone',
        },
        passportInfo: {
          rules: 'required',
          text: 'Passport Information',
          type: 'json',
          value: {
            number: null,
            issuedCountry: null,
            expiryDate: null,
          },
        },
        emergencyContactPersons: {
          rules: 'required|required2',
          type: 'json',
          value: [
            {
              name: null,
              relationship: null,
              tel: null,
            },
            {
              name: null,
              relationship: null,
              tel: null,
            },
          ],
          customRules: {
            required2({value}) {
              return Object.values(value[0]).every(v => v)
            },
          },
          messages: {
            required2({value}) {
              for (const key in value[0]) {
                if (!value[0][key]) {
                  return `The ${key} of emergency contact person 1 is required`
                }
              }
            },
          },
        },
        declared: {
          rules: 'required|accepted',
        },
      },
      validation: {},
      loading: false,
    }
  },
  computed: {
    // raise
    passportInfo() {return this.fields.passportInfo.value},
    ecp() {return this.fields.emergencyContactPersons.value},
  },
  // watch: {},
  methods: {
    save() {
      if (this.loading) {
        return
      }
      this.$checkValidation(this.validation).then(async requestData => {
        this.loading = true
        await this.$apiPost(`/user/profile`, {data: requestData})
        await this.$store.dispatch('auth/fetchUser')
        this.$alert(`Saved Successfully`, '')
        this.loading = false
      }).catch(e => {
        this.loading = false
        return Promise.reject(e)
      })
    }
  },
  created() {
    ut.setDataToFields(this.data, this.fields)
  },
  mounted() {
    this.$validate(this.validation, this.fields)
    this.$testPanel({
      fill: () => {
        this.$testFill(this.fields)
        this.fields.gender.value = 'male'
        this.fields.nationality.value = 'US'
        this.fields.phone.value = '+1 214214'
        this.fields.countryOfResidence.value = 'US'
        this.passportInfo.number = 'test'
        this.passportInfo.issuedCountry = 'US'
        this.passportInfo.expiryDate = new Date
        this.ecp[0].name = 'test'
        this.ecp[0].relationship = 'test'
        this.ecp[0].tel = '+1234125'
      },
    })
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.student-profile{
  ._1{
    display: flex;
    justify-content: space-between;
  }
  ._1r{
    flex-grow: 1;
  }
  .avatar-uploader{
    $side: 145px;
    width: $side;
    height: $side;
    flex-shrink: 0;
  }
  @media(max-width: $small) {
    ._1{
      display: block;
    }
    .avatar-uploader{
      margin: 0;
      margin-bottom: 1em;
    }
  }
  .declare{
    font-size: 13px;
    display: flex;
  }
}
</style>
