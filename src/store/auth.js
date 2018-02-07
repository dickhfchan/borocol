export default {
  visible: false,
  mode: 'login',
  role: 'student',
  loginFields: {
    email: {
      rules: 'required|email',
    },
    password: {
      rules: 'required',
    },
    remember: {
      value: false,
    },
  },
  loginValidation: {},
  registrationFields: {
    email: {
      rules: 'required|email',
    },
    firstName: {
      rules: 'required',
    },
    lastName: {
      rules: 'required',
    },
    password: {
      rules: 'required|lengthBetween:5,16',
    },
    passwordConfirmation: {
      rules: 'required|same:password',
    },
    agreed: {
      rules: 'required|accepted',
    },
  },
  registrationValidation: {},

  show(mode, role) {
    if (mode) {
      this.mode = mode
    }
    if (role) {
      this.role = role
    }
    this.visible = true
  },
}
