<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="page_title_div">
    <h1 class="title">{{ msg }}</h1>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  padding-left: 10px;
  /* padding-top: 10px; */

  top: -10px;
}

</style>
