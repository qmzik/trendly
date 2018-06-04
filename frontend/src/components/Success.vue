<template>
    <p>УСПЕХ</p>
</template>

<script>
  import { API_ROUTE } from '../consts/routes'

  export default {
    name: 'Success',
    mounted: function () {
      let res = location.hash;
      res = res.replace('#/access_token=', '');
      res = res.replace('expires_in=', '');
      res = res.replace('user_id=', '');
      res = res.split('&');
      let data = { userId: localStorage.userId, accessToken: localStorage.accessToken, vkApiToken: res[0], vkUserId: res[2] };
      console.log(data)
      this.$http.post(API_ROUTE + '/user/settings/vk_key', data, function () {
        console.log('Success')
      }, function () {
        console.log('Rejected')
      });
    }
  }
</script>

<style scoped>

</style>
