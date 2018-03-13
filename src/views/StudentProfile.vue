<template lang="pug">
include ../common.pug
.StudentProfile
  .container
    .content-card
      h1.content-card-title Profile
      form.content-card-body.flex(@submit.prevent="save")
        .form-left
          ._1
            .avatar.mrm
              ImageUploader.mrl(:aspectRatio="1/1" v-model="fields.avatar.value" title="Upload Photo")
            .avatar-right
              .form-group
                label Name on Passport
                .flex
                  +inputLg(placeholder="* First Name" v-model="fields.firstName.value")
                  .space
                  +inputLg(placeholder="Middle Name" v-model="fields.middleName.value")
                  .space
                  +inputLg(placeholder="* Last Name" v-model="fields.lastName.value")
                .flex.mtm
                  +formGroup('fields.gender')
                    +selectLg(v-model="fields.gender.value")
                      option(v-for="item in $state.genderOptions" :value="item.value") {{item.text}}
                  .space
                  +formGroup('fields.birthday')
                    DatePicker(v-model="fields.birthday.value" :format="dateFormat")
                  .space
                  +formGroup('fields.nationality')
                    +selectLg(v-model="fields.nationality.value")
                      option(value="USA") USA
          .flex
            +formGroup('fields.countryOfResidence')
              +selectLg(v-model="fields.countryOfResidence.value")
                option(value="USA") USA
            .space
            +formGroup('fields.email').flex-1
              +inputLg(v-model="fields.email.value")
            .space
            +formGroup('fields.phone').phone
              .input-group
                .input-group-addon +1(917)
                +inputLg(v-model="fields.phone.value")
          +formGroup('fields.passportInfo').passport
            .flex
              +inputLg(placeholder="Passport Number" v-model="fields.passportInfo.value.number")
              .space
              +inputLg(placeholder="Issued Country" v-model="fields.passportInfo.value.issuedCountry")
              .space
              DatePicker.expiry-date(placeholder="Expiry Date" :format="dateFormat" v-model="fields.passportInfo.value.expiryDate")
        .form-right
          .form-group
            label * Emergency Contact Person 1
            +inputLg(placeholder="Name" v-model="ecp[0].name")
            .flex.mtm
              +inputLg(placeholder="Relationship" v-model="ecp[0].relationship")
              .space
              +inputLg(placeholder="Tel" v-model="ecp[0].tel")
          .form-group.mtm
            label Emergency Contact Person 2
            +inputLg(placeholder="Name" v-model="ecp[1].name")
            .flex.mtm
              +inputLg(placeholder="Relationship" v-model="ecp[1].relationship")
              .space
              +inputLg(placeholder="Tel" v-model="ecp[1].tel")
          .declare.mtm.flex
            Checkbox.flex-0(v-model="fields.declared.value")
            .mlm
              p I hereby declare that all information provided above is true and accurate.
              p I agree to <a href="#">Borocol’s Terms of Service</a> and undestating <a href="#">the purpose of collecting personal data</a>.
          .mtm
            button.btn.btn-primary.btn-lg.btn-block Save
</template>

<script>
import ImageUploader from '@/components/ImageUploader';
import DatePicker from '@/components/DatePicker';
import {newDate, checkValidation} from '@/utils'
import {snakeCase} from 'helper-js'
export default {
  metaInfo () {
    return {
      title: this.$state.resolveTitle('Profile'),
    }
  },
  components: {ImageUploader, DatePicker},
  data() {
    return {
      dateFormat: 'MMM dd yyyy',
      fields: {
        avatar: {
          rules: 'required',
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
          rules: 'required|numeric',
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
        emergencyContactPerson: {
          rules: 'required',
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
        },
        declared: {
          rules: 'required|accepted',
        },
      },
      validation: {},
      saving: false,
    }
  },
  computed: {
    // raise
    ecp: {
      get() {return this.fields.emergencyContactPerson.value},
      set(value) {this.fields.emergencyContactPerson.value = value},
    },

  },
  // watch: {},
  methods: {
    save() {
      if (this.saving) {
        return
      }
      checkValidation(this.validation).then(async requestData => {
        this.saving = true
        if (Object.values(this.fields.passportInfo.value).some(v => !v)) {
          this.$alert(`Passport info is required`);
        } else if (Object.values(this.fields.emergencyContactPerson.value[0]).some(v => !v)) {
          this.$alert(`Emergency contact person 1 is required`);
        } else {
          Object.values(this.fields).forEach(fld => {
            switch (fld.type) {
              case 'date':
                  requestData[fld.name] = parseInt(newDate(requestData[fld.name]).getTime() / 1000)
                break;
              case 'json':
                  requestData[fld.name] = JSON.stringify(requestData[fld.name])
                break;
            }
          })
          await this.$apiPost(`/student_profile/store`, requestData)
          this.$alert(`Saved Successfully`)
        }
        this.saving = false
      }).catch(e => {
        this.saving = false
        throw e
      })
    }
  },
  // created() {},
  mounted() {
    this.$validate(this.validation, this.fields)
    window.StudentProfile  = {
      fill: () => {
        Object.values(this.fields).forEach(fld => {
          if (fld.type === 'date') {
            fld.value = '2018-01-01'
          } else if (fld.name === 'declared') {
            fld.value = true
          } else if (fld.name === 'passportInfo') {
            fld.value =  {
              number: 'safsagsa',
              issuedCountry: 'asfgasg',
              expiryDate: '2018-01-01',
            }
          } else if (fld.type === 'json') {
            // emergencyContactPerson
            for (const key in fld.value[0]) {
              fld.value[0][key] = 'anything'
            }
          } else {
            fld.value = 'anything'
          }
        })
      }
    }
  },
}
</script>

<style lang="scss">
.StudentProfile{
  background-image: url(~@/assets/img/profile-bg.jpg);
  background-position: center;
  background-size: cover;
  .container{
    width: 1400px;
    padding: 0;
  }
  .form-right{
    width: 380px;
    margin-left: 70px;
  }
  ._1{
    display: flex;
  }
  .avatar{
    .ImageUploader{
      $side: 160px;
      width: $side;
      height: $side;
    }
  }
  .phone{
    width: 300px;
  }
  .expiry-date{
    width: 30%;
    flex-shrink: 0;
  }
  .declare{
    font-size: 13px;
    a{
      font-weight: 500;
    }
  }
}
</style>
