<template>
   <div id="app">
      <router-view />
   </div>
</template>

<script setup>
// Composition API ishlatilgan, lekin App.vue faqat root, logic yo‘q
</script>

<style>
/* Global style */
body {
   font-family: Arial, sans-serif;
   margin: 0;
   padding: 0;
}

#app {
   max-width: 1200px;
   margin: 0 auto;
   padding: 20px;
}
</style>
