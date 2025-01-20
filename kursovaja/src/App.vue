<script>
import Header from './components/Header.vue';

export default {
  components: {
    Header,
  }
}

</script>

<template>
  <div class="wrapper p-2">
    <Header />
    <div class="content">
      <router-view>
      </router-view>
    </div>


  </div>
</template>

<style scoped></style>
