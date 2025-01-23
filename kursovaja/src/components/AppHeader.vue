<template>
  <div class="container">
    <header
      class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none">
        <h3>Золотые ручки</h3>
      </a>

      <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
        <li>
          <router-link to="/" class="nav-link px-2 link-dark">Главная</router-link>
        </li>
        <li>
          <router-link to="/search" class="nav-link px-2 link-dark">Поиск</router-link>
        </li>
        <li>
          <router-link to="/faqs" class="nav-link px-2 link-dark">FAQs</router-link>
        </li>
      </ul>

      <div class="col-md-3 text-end">
        <span v-if="isAuthenticated">
          {{ user.username }} <!-- Используем геттер username -->
          <button @click="logout" class="logout-button">Выйти</button>
        </span>
        <span v-else>
          <router-link to="/login" class="btn btn-outline-warning me-2">Login</router-link>
          <router-link to="/register" class="btn btn-warning">Sign-up</router-link>
        </span>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    user() {
      return this.$store.getters.user; // Получаем объект пользователя
    },
  },
  methods: {
    async logout() {
      try {
        await this.$store.dispatch('logout');
        this.$router.push('/login'); // Перенаправление на страницу входа после выхода
      } catch (error) {
        console.error('Ошибка при выходе:', error);
      }
    },
  },
};
</script>

<style scoped>
.logout-button {
  background-color: transparent;
  border: none;
  color: #dc3545;
  cursor: pointer;
  margin-left: 10px;
}

.logout-button:hover {
  text-decoration: underline;
}
</style>