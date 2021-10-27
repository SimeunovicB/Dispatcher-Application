<template>
  <div v-bind:style="{'background-color': bgColor}">
    {{ message }}
  </div>
    <div @mouseover="actionHover()">Click Me!</div>

    <div class="tooltip">Hover over me
  <span class="tooltiptext">Tooltip text</span>
</div>
</template>

<script>
export default {
  data() {
    return {
      message: "Hello friend",
      bgColor: "#ccc"
    };
  },
  methods: {
      actionHover() {
          this.bgColor = 'red';
      }
  }
};
</script>

<style>
</style>