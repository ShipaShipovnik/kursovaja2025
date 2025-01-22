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
                    {{ username }}
                    <button v-if="isAuthenticated" @click="logout" class="logout-button">Выйти</button>

                </span>
                <span v-else>
                    <router-link to="/login" class="btn btn-outline-warning me-2">
                        Login
                    </router-link>
                    <router-link to="/register" class="btn btn-warning">
                        Sign-up
                    </router-link>
                </span>
            </div>
        </header>
    </div>
</template>

<script>
export default {
    computed: {
        isAuthenticated() {
            return this.$root.isAuthenticated;
        },
        username() {
            return this.$root.username;
        },
    },
    methods: {
        logout() {
            this.$root.logout();
        },
    },
};
</script>

<style></style>