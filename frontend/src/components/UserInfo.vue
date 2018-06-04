<template>
  <div class="row">
    <at-dropdown class="username col-md-12 col-xs-12">
      <at-button>John Doe<i class="icon icon-chevron-down"/></at-button>
      <at-dropdown-menu slot="menu">
        <at-dropdown-item @click.native="logOut()" name="beijin" divided>Log out</at-dropdown-item>
      </at-dropdown-menu>
    </at-dropdown>
    <div class="userPhoto"></div>
  </div>
</template>

<script>
    import { API_ROUTE } from '../consts/routes'
    import { WRONG_LOGOUT } from '../consts/userNotices'

    export default {
        name: "UserInfo",
        methods: {
          logOut: function () {
            let logOutData = { userId: localStorage.userId, accessToken: localStorage.accessToken }
            this.$http.post(API_ROUTE + 'user/logout', logOutData).then(function (res) {
              this.$router.push({ name: 'Landing', path: '/' });
              localStorage.clear();
            }, function (res) {
              this.$Notify({
                title: "Ошибка",
                message: WRONG_LOGOUT,
                type: "error"
              });
            })
          }
      }
    }
</script>

<style scoped>
  .username {
    padding-top: 12px;
  }

  .username i {
    margin-left: 7px;
  }

  .username .at-btn {
    border: none;
  }

  .userPhoto {
    width: 40px;
    height: 40px;
    border: solid 1px white;
    border-radius: 50%;
    background-image: url("../assets/profile_photo_test.jpg");
    background-size: cover;
    background-position: center;
    margin-top: 3px;
  }
</style>
