<script>
import AppHeader from './components/AppHeader.vue';
import api from './api';
export default {
  components: {
    AppHeader,
  },
  data() {
    return {
      isAuthenticated: false,
      username: '',
    };
  },
  created() {
    this.checkAuth();
  },
  methods: {
    async checkAuth() {
      try {
        const response = await api.checkAuth();
        this.isAuthenticated = true;
        this.username = response.data.username;
      } catch (error) {
        this.isAuthenticated = false;
        this.username = '';
      }
    },

    logout() {
      this.isAuthenticated = false;
      this.username = '';
      this.$router.push('/login');
    },
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
