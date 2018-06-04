<template>
    <div class="project-card">
      <div>
        <h1>{{ title }}</h1>
        <h4>{{ publicLink }}</h4>
      </div>
      <span>Average CTR: {{ ctr }}</span>
    </div>
</template>

<script>
    export default {
      name: "ProjectCard",
      data() {
        return {
          title: "Медуза",
          publicLink: "vk.com/meduzaproject",
          ctr: "1.32"
        }
      }
    }
</script>

<style scoped>
  .project-card {
    width: 300px;
    height: 300px;
    border: 1px black solid;
    padding: 30px;
    text-align: left;
  }

  h1 {
    font-size: 25px;
  }

  h4 {
    font-size: 16px;
    color: #b2b2b2;
  }
</style>
