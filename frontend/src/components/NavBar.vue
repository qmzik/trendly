<template>
  <header class="container">
    <div class="row">
      <nav class="col-md-24 col-xs-24">
        <router-link to="Dashboard">
        <MenuButton class="menuButton" :class="{ active: whichActive === 1 }" @click.native="whichActive=1">
          <template slot="icon"><i class="icon icon-bar-chart-2"></i></template>
          <span>Dashboard</span>
        </MenuButton>
        </router-link>
        <router-link to="">
        <MenuButton class="menuButton" :class="{ active: whichActive === 2 }" @click.native="whichActive=2">
          <template slot="icon"><i class="icon icon-refresh-ccw"></i></template>
          <span>Tasks</span>
        </MenuButton>
        </router-link>
        <router-link to="Settings">
        <MenuButton class="menuButton" :class="{ active: whichActive === 3 }" @click.native="whichActive=3">
          <template slot="icon"><i class="icon icon-settings"></i></template>
          <span>Settings</span>
        </MenuButton>
        </router-link>
        <router-link to="">
        <MenuButton class="menuButton" :class="{ active: whichActive === 4 }" @click.native="whichActive=4">
          <template slot="icon"><i class="icon icon-message-square"></i></template>
          <span>Support</span>
        </MenuButton>
        </router-link>
      </nav>
    </div>
  </header>
</template>

<script>
  import MenuButton from './controls/MenuButton'
  export default {
    name: 'NavBar',
    components: {MenuButton},
    data() {
      return {
        whichActive: 1
      }
    }
  }
</script>

<style scoped>
  header {
    height: 100vh;
    background-color: #959595;
    padding-top: 25vh;
  }

  .menuButton {
    font-size: 20px;
    padding-left: 30px;
    background-color: #6E6E6E;
    color: white;
  }

  .active {
    border-left: 12px solid #A8A2E8;
    background-color: #565656;
  }

  .icon {
    color: #A8A2E8;
    margin-right: 20px;
    margin-top: 3px;
  }
</style>
