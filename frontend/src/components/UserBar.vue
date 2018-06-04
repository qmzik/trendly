<template>
  <div class="userBar">
    <div class="col-md-offset-14 col-md-4 col-xs-offset-13 col-xs-10 icons">
      <i class="col-md-offset-2 col-md-11 col-xs-11 icon icon-message-circle"></i>
      <i class="col-md-11 col-xs-11 icon icon-bell"></i>
    </div>
    <UserInfo class="col-md-6"></UserInfo>
  </div>
</template>

<script>
    import UserInfo from "./UserInfo";
    export default {
      name: "UserBar",
      components: {UserInfo}
    }
</script>

<style scoped>
 .userBar {
   display: inline-flex;
   height: 50px;
   width: 100%;
   background-color: white;
   border-bottom: solid 1px darkgrey;
 }

 .icons {
   padding-top: 15px;
 }

  .icon {
    color: #A8A2E8;
    margin-right: 20px;
    margin-top: 3px;
    font-size: 20px;
    padding-top: 8px;
  }
</style>
