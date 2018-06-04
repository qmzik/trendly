<template>
<at-button @click="vkAuth">VK OAuth</at-button>
</template>

<script>
    export default {
        name: "Settings",
      methods: {
          vkAuth: function () {
            window.open('https://oauth.vk.com/authorize?client_id=6345206&display=popup&redirect_uri=http://localhost:8080/&response_type=token&v=5.75');
          }
      }
    }
</script>

<style scoped>

</style>
