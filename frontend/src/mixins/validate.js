import { EMAIL_REGEXP, PASSWORD_REGEXP } from '../consts/regExp'

export let validateEmail = {
  data() {
    return {
      email: ""
    }
  },
  computed: {
    isEmailValid: function () {
      return EMAIL_REGEXP.test(this.email)
    }
  }
};

export let validatePassword = {
  data() {
    return {
      password: ""
    }
  },
  computed: {
    isPasswordValid: function () {
        return PASSWORD_REGEXP.test(this.password)
    }
  }
};


