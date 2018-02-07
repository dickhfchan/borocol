<template lang="pug">
include ../common.pug
.Settings
  .container
    .content-card
      h1.content-card-title Settings
      form.content-card-body
        .form-group
          label Privacy (Visible to other students)
          div
            Checkbox.mrm(v-model="fields.profile.value")
            span.mrl Profile
            Checkbox.mrm(v-model="fields.likedCourses.value")
            span Liked Courses
        +formGroup("fields.oldPassword")
          +inputLg(type="password")
        +formGroup("fields.newPassword")
          +inputLg(type="password")
        +formGroup("fields.newPasswordConfirmation")
          +inputLg(type="password")
        button.btn.btn-primary.btn-lg.btn-block Save Change
</template>

<script>

export default {
  components: {},
  data() {
    return {
      validation: {},
      fields: {
        profile: {
          value: true,
        },
        likedCourses: {
          value: false,
        },
        oldPassword: {
          rules: 'required',
          text: 'Old Password',
        },
        newPassword: {
          rules: 'required|minLength: 5',
          text: 'New Password',
        },
        newPasswordConfirmation: {
          rules: 'required|minLength: 5|same:newPassword',
          text: 'New Password Confirmation',
        },
      },
    }
  },
  // computed: {},
  // watch: {},
  methods: {
  },
  created() {
    this.$validate(this.validation, this.fields)
  },
  mounted() {
  },
}
</script>

<style lang="scss">
.Settings{
  background-image: url(~@/assets/img/settings-bg.jpg);
  background-position: center;
  background-size: cover;
  .container{
    width: 800px;
    padding: 0;
  }
}
</style>
