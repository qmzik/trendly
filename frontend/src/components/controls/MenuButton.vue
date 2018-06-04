<template>
    <div id="menuButton" class="row">
      <slot name="icon"></slot>
      <slot></slot>
    </div>
</template>

<script>
  export default {
    name: 'MenuButton',
  }
</script>

<style scoped>
  #menuButton {
    height: 50px;
    padding-top: 10px;
    cursor: pointer;
  }
</style>
