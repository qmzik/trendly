<template>
  <div id="signUp">
    <at-button @click="showRegistration=true" type="primary">Зарегистрироваться</at-button>
    <at-modal v-model="showRegistration" title="Регистрация">
      <div class="row">
        <form class="col-xs-18 col-md-18 flex-center col-xs-offset-2 col-md-offset-2">
          <div class="row input-field">
            <label class="col-xs-11 col-md-11">Имя:</label>
            <at-input v-model="firstName" class="col-xs-11 col-md-11" placeholder="Имя"></at-input>
            <HelpIcon :if-empty="!firstName" :if-valid="isFirstNameCorrect" :if-invalid="isFirstNameCorrect" :hint="FIRST_NAME_EXAMPLE"></HelpIcon>
          </div>
          <div class="row input-field">
            <label class="col-xs-11 col-md-11">Фамилия:</label>
            <at-input v-model="secondName" class="col-xs-11" placeholder="Фамилия"></at-input>
            <HelpIcon :if-empty="!secondName" :if-valid="isSecondNameCorrect" :if-invalid="isSecondNameCorrect" :hint="SECOND_NAME_EXAMPLE"></HelpIcon>
          </div>
          <div class="row input-field">
            <label class="col-xs-11 col-md-11">Введите E-mail:</label>
            <at-input v-model="email" class="col-xs-11 col-md-11" placeholder="E-mail"></at-input>
            <HelpIcon :if-empty="!email" :if-valid="isEmailValid" :if-invalid="isEmailValid" :hint="EMAIL_EXAMPLE"></HelpIcon>
          </div>
          <div class="row input-field">
            <label class="col-xs-11 col-md-11">Введите пароль:</label>
            <at-input type="password" v-model="password" class="col-xs-11 col-md-11" placeholder="Пароль"></at-input>
            <HelpIcon :if-empty="!password" :if-valid="isPasswordValid" :if-invalid="isPasswordValid" :hint="CORRECT_PASSWORD_NOTICE"></HelpIcon>
          </div>
          <div class="row input-field">
            <label class="col-xs-22 col-md-22">Я прочитал и согласен со всеми правилами</label>
            <at-checkbox v-model="isUserAgreeWithRules" class="col-xs-2 col-md-2"></at-checkbox>
          </div>
        </form>
      </div>
      <div slot="footer">
        <at-button @click="showRegistration=false">Отмена</at-button>
        <at-button :disabled="!isAllCorrect" type="primary" @click="sendData">Зарегистрироваться</at-button>
      </div>
    </at-modal>
  </div>
</template>

<script>
  import md5 from 'md5'
  import { EMAIL_EXAMPLE, CORRECT_PASSWORD_NOTICE, FIRST_NAME_EXAMPLE, SECOND_NAME_EXAMPLE, ACTIVATION_MAIL } from '../consts/userNotices'
  import { NAME_REGEXP } from '../consts/regExp'
  import { validateEmail, validatePassword } from '../mixins/validate'
  import HelpIcon from "./HelpIcon";
  import { API_ROUTE } from '../consts/routes'
    export default {
        name: "SignUp",
      components: {HelpIcon},
      mixins: [validateEmail, validatePassword],
      constants: {
        CORRECT_PASSWORD_NOTICE,
        EMAIL_EXAMPLE,
        FIRST_NAME_EXAMPLE,
        SECOND_NAME_EXAMPLE,
        ACTIVATION_MAIL
      },
      data () {
          return {
            showRegistration: false,
            firstName: "",
            secondName: "",
            isUserAgreeWithRules: "",
          }
      },
      computed: {
        isFirstNameCorrect: function () {
          return NAME_REGEXP.test(this.firstName)
        },
        isSecondNameCorrect: function () {
          return NAME_REGEXP.test(this.secondName)
        },
        isAllCorrect: function () {
          return this.isPasswordValid && this.isEmailValid && this.isUserAgreeWithRules && this.isFirstNameCorrect && this.isSecondNameCorrect;
        },
        passwordHash: function () {
          return md5(this.password);
        }
      },
      methods: {
        sendData: function () {
          let data = { firstName: this.firstName, secondName: this.secondName, email: this.email, passwordHash: this.passwordHash };

          this.$http.post(API_ROUTE + 'user/register', data).then(function (res) {
            console.log(res);
            if(res.ok) {
              this.$Notify({
                title: "Успех",
                message: ACTIVATION_MAIL + this.email,
                type: "success"
              });
              this.firstName = "";
              this.secondName = "";
              this.email = "";
              this.password = "";
              this.isUserAgreeWithRules = false;
              this.showRegistration = false;
            } else {
              this.$Notify({
                title: "Ошибка",
                message: "Пользователь с таким электронным адресом уже зарегистрирован",
                type: "error"
              });
            }
          });
        }
      },
      watch: {
        firstName: function () {
          this.firstName ? this.firstName = this.firstName[0].toUpperCase() + this.firstName.slice(1) : null;
        },
        secondName: function () {
          this.secondName ? this.secondName = this.secondName[0].toUpperCase() + this.secondName.slice(1) : null;
        }
      }
    }
</script>

<style scoped>
  #signUp {
    display: inline-block;
  }

 .input-field {
   margin-top: 30px;
 }

  label {
    text-align: left;
    font-weight: bold;
  }
</style>
