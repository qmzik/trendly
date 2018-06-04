<template>
  <div>
    <SignIn></SignIn>
    <SignUp></SignUp>
  </div>
</template>

<script>
    import SignIn from "./components/SignIn";
    import SignUp from "./components/SignUp";
    export default {
        name: "Landing",
      components: {SignUp, SignIn}
    }
</script>

<style scoped>

</style>
