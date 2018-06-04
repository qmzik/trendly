<template>
  <div>
    <ProjectCard></ProjectCard>
  </div>
</template>

<script>
    import ProjectCard from "./ProjectCard";
    export default {
      name: "Dashboard",
      components: {ProjectCard},
      data () {
        return {
          cards: []
        }
      },
      methods: {
        AddCard: function () {
          this.cards.push({ type: 'Name' })
        }
      }
    }
</script>

<style scoped>

</style>
