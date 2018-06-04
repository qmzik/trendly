<template>
    <div id="signIn">
      <at-button @click="showSignIn=true">Войти</at-button>
      <at-modal v-model="showSignIn" title="Вход">
        <div class="row">
          <form class="col-md-18 col-xs-18 flex-center col-md-offset-2 col-xs-offset-2">
            <div class="row input-field">
              <label class="col-md-11 col-xs-11">Введите E-mail:</label>
              <at-input v-model="email" class="col-md-11" placeholder="E-mail"></at-input>
              <HelpIcon :if-empty="!email" :if-valid="isEmailValid" :if-invalid="isEmailValid" :hint="EMAIL_EXAMPLE"></HelpIcon>
            </div>
            <div class="row input-field">
              <label class="col-md-11 col-xs-11">Введите пароль:</label>
              <at-input type="password" v-model="password" class="col-md-11 col-xs-11" placeholder="Пароль"></at-input>
              <HelpIcon :if-empty="!password" :if-valid="isPasswordValid" :if-invalid="isPasswordValid" :hint="CORRECT_PASSWORD_NOTICE"></HelpIcon>
            </div>
          </form>
        </div>
        <div slot="footer">
          <at-button @click="showSignIn=false">Отмена</at-button>
          <at-button :disabled="!isEmailValid || !isPasswordValid" type="primary" @click="onSubmit">Войти</at-button>
        </div>
      </at-modal>
    </div>
</template>

<script>
  import { CORRECT_PASSWORD_NOTICE, EMAIL_EXAMPLE, WRONT_CREDENTIALS } from '../consts/userNotices'
  import { validateEmail, validatePassword } from '../mixins/validate'
  import HelpIcon from "./HelpIcon";
  import md5 from 'md5'
  import { API_ROUTE } from '../consts/routes'
    export default {
      constants: {
        CORRECT_PASSWORD_NOTICE,
        EMAIL_EXAMPLE,
        WRONT_CREDENTIALS
      },
      components: {HelpIcon},
      mixins: [validateEmail, validatePassword],
        name: "SignIn",
      data () {
          return {
            showSignIn: false,
            password: '',
            email: ''
          }
      },
      computed: {
        passwordHash: function () {
          return md5(this.password);
        }
      },
      methods: {
          onSubmit: function () {
            let data = { email: this.email, passwordHash:  this.passwordHash};
            this.$http.post(API_ROUTE + 'user/auth', data).then(function (res) {
              localStorage.userId = res.body.userId;
              localStorage.accessToken = res.body.accessToken;
              console.log(res);
              this.$router.push({ name: 'Dashboard', params: { id: localStorage.userId }});
            }, function () {
              this.$Notify({
                title: "Ошибка",
                message: WRONT_CREDENTIALS,
                type: "error"
              });
            });
          }
      },
    }
</script>

<style scoped>
  #signIn {
    display: inline-block;
}
  .input-field {
    margin-top: 30px;
  }
</style>
