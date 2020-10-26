<template>
  <div>
    <Header />
    <div class="container">
      <h1>Retro Mailer</h1>
    </div>
  </div>
</template>

<script>
import Header from '../components/layout/Header.vue';

export default {
  name: 'Home',
  components: {
    Header,
  },
};
</script>

<style scoped>
  .container {
    margin-top: 2rem;
  }
</style>
