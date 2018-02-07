<template lang="pug">
include ../common.pug
.SchoolProfile
  .container
    .content-card
      h1.content-card-title Profile
      form.content-card-body(@submit.prevent="save")
        el-row(:gutter="50")
          el-col(:span="12")
            +formGroup('fields.name')
              +inputLg(v-model="fields.name.value")
            +formGroup('fields.address')
              +inputLg(v-model="fields.address.value")
            el-row(:gutter="10")
              el-col(:span="12")
                +formGroup('fields.address')
                  +inputLg(v-model="fields.address.value")
              el-col(:span="12")
                +formGroup('fields.country')
                  +selectLg(v-model="fields.country.value")
            +formGroup('fields.email')
              +selectLg(v-model="fields.email.value")
            +formGroup('fields.introduction')
              +textarea(v-model="fields.introduction.value" rows="5")
            +formGroup('fields.officialWebsite')
              +inputLg(v-model="fields.officialWebsite.value")
            +formGroup('fields.businessRegistrationDocument')
              //- to do, extract as a component
              .flex
                +inputLg(disabled="disabled" :value="fields.businessRegistrationDocumentName.value")
                UploadBtn.btn.btn-default.flex-s0.mlm(
                  ref="uploadBtn"
                  v-model="fields.businessRegistrationDocument.value"
                  :mimes="['application/pdf']"
                  @change="fields.businessRegistrationDocumentName.value=$refs.uploadBtn.files[0].name"
                )
          el-col(:span="12")
            .form-group
              label * Contact Person 1
              el-row(:gutter="10")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[0].lastName" placeholder="Last Name")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[0].firstName" placeholder="First Name")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[0].title" placeholder="Title(e.g. Admin)")
              el-row.mtm(:gutter="10")
                el-col(:span="16")
                  +inputLg(v-model="fields.contactPerson.value[0].email" placeholder="Email")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[0].tel" placeholder="Tel")
            .form-group
              label Contact Person 2
              el-row(:gutter="10")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[1].lastName" placeholder="Last Name")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[1].firstName" placeholder="First Name")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[1].title" placeholder="Title(e.g. Admin)")
              el-row.mtm(:gutter="10")
                el-col(:span="16")
                  +inputLg(v-model="fields.contactPerson.value[1].email" placeholder="Email")
                el-col(:span="8")
                  +inputLg(v-model="fields.contactPerson.value[1].tel" placeholder="Tel")
            .form-group
              label Payment Gateway
              button.stripe-btn.btn.btn-default.btn-lg.mlm(type="button") Setup <b> Stripe </b> Account
            el-row.mtm(:gutter="10")
              el-col(:span="5")
                .form-group
                  label * Upload Logo
                  .mts
                    ImageUploader(v-model="fields.avatar.value")
              el-col(:span="19")
                .form-group
                  label * Upload School Photos (min. 3)
                  .mts
                    MultipleImageUploader(v-model="fields.photos.value" :boxSpace="10")
            .flex.mts
              Checkbox.flex-s0(v-model="fields.agreed.value")
              .f13.mlm By signing up, I agree to Borocol’s Terms of Service, Payments Terms of Service, Privacy Policy, Refund Policy, and Host Guarantee Terms.
            button.btn.btn-primary.btn-lg.btn-block.mtm Submit
</template>

<script>
import ImageUploader from '@/components/ImageUploader';
import MultipleImageUploader from '@/components/MultipleImageUploader';
import UploadBtn from '@/components/UploadBtn';
import DatePicker from '@/components/DatePicker';
import {newDate} from '@/utils'
import {snakeCase, arrayLast} from 'helper-js'
export default {
  components: {ImageUploader, MultipleImageUploader, UploadBtn, DatePicker},
  data() {
    return {
      dateFormat: 'MMM dd yyyy',
      fields: {
        name: {
          rules: 'required',
          text: '‘Name of School / Institution',
        },
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
        email: {
          rules: 'required|email',
          text: 'Email(This will be used for receiving notifications)',
        },
        introduction: {
          rules: 'required',
          text: 'Introduction',
        },
        officialWebsite: {
          rules: 'required',
          text: 'Official Website'
        },
        businessRegistrationDocumentName: {
        },
        businessRegistrationDocument: {
          rules: 'required',
          text: 'Business Registration Document(BR)',
        },
        contactPerson: {
          rules: 'required',
          type: 'json',
          value: [
            {
              firstName: null,
              lastName: null,
              title: null,
              email: null,
              tel: null,
            },
            {
              firstName: null,
              lastName: null,
              title: null,
              email: null,
              tel: null,
            },
          ],
        },
        avatar: {
          rules: 'required',
        },
        photos: {
          rules: 'required',
          value: [],
        },
        agreed: {
          rules: 'required|accepted',
        },
      },
      validation: {},
      saving: false,
    }
  },
  computed: {
  },
  // watch: {},
  methods: {
    save() {},
  },
  // created() {},
  mounted() {
    this.$validate(this.validation, this.fields)
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.SchoolProfile{
  .stripe-btn{
    @include btnColors(rgb(0, 148, 232), #fff);
    text-transform: none;
    font-weight: 400;
    font-size: 14px;
    padding: 15px 50px;
    b{
      font-size: 20px;
    }
  }
}
</style>
