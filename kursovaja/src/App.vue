<script>
import AppHeader from './components/AppHeader.vue';

export default {
  components: {
    AppHeader,
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated; // Используем геттер из Vuex
    },
    username() {
      return this.$store.getters.user?.username; // Используем геттер из Vuex
    },
  },
  created() {
    if (this.isAuthenticated) {
      this.$store.dispatch('fetchUser'); // Загружаем данные пользователя при создании компонента
    }
  },
};

</script>

<template>
  <div class="wrapper p-2">
    <AppHeader />
    <div class="content">
      <router-view>
      </router-view>
    </div>


  </div>
</template>

<style scoped></style>
