<template>
  <at-popover class="at-popover" trigger="hover" :content="hint">
    <i v-if="ifEmpty" class="icon icon-help-circle"></i>
    <i v-else-if="ifValid" class="icon icon-check-circle col-md-2"></i>
    <i v-else="ifInvalid" class="icon icon-x-circle"></i>
  </at-popover>
</template>

<script>
    export default {
        name: "HelpIcon",
        props: ['ifEmpty', 'ifValid', 'ifInvalid', 'hint']
    }
</script>

<style scoped>
  .at-popover {
    font-size: 20px;
  }

  .icon-help-circle {
    color: #87b1ff;
  }

  .icon-check-circle {
    color: #25ba21;
  }

  .icon-x-circle {
    color: #ff2723;
  }
</style>
