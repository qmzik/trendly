<template>
  <div class="row">
    <NavBar class="col-md-6 col-xs-6"></NavBar>
    <div style="padding: 0" class="col-md-18 col-xs-18">
      <UserBar></UserBar>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
    import Dashboard from "./Dashboard";
    import UserBar from "./UserBar";
    import NavBar from "./NavBar"
    export default {
        name: "InterfaceBoard",
      components: {UserBar, Dashboard, NavBar}
    }
</script>

<style scoped>

</style>
