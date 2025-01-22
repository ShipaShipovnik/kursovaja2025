<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Авторизация</h1>
        <div class="login-form text-center">
            <form @submit.prevent="loginUser" class="form">
                <label class="form-label">
                    Логин:
                    <input class="form-control" type="text" v-model="credentials.username" required />
                </label>
                <br />
                <label class="form-label">
                    Пароль:
                    <input class="form-control" type="password" v-model="credentials.password" required />
                </label>
                <br />
                <button type="submit" class="btn btn-warning ">Войти</button>
            </form>
            <p class="text-muted" mt-4>
                Нет аккаунта? <router-link to="/register" class="text-warning">Регистрация.</router-link>
            </p>
        </div>
    </div>
</template>

<script>
import api from '@/api';
import Cookies from 'js-cookie';

export default {
    data() {
        return {
            credentials: {
                username: '',
                password: '',
            }
        }
    },
    methods: {
        async loginUser() {
            try {
                const credentials = {
                    username: this.credentials.username,
                    password: this.credentials.password,
                };
                const response = await api.loginUser(credentials);
                console.log('Успешная авторизация', response.data);

                // Обновляем состояние в корневом компоненте
                this.$root.isAuthenticated = true;
                this.$root.username = response.data.username;

                // Перенаправление на главную страницу
                this.$router.push('/');
            } catch (error) {
                console.error('Ошибка авторизации', error);
            }
        },
        async logout() {
            try {
                await api.logoutUser();
                this.$router.push('/login');
            } catch (error) {
                console.error('Ошибка при выходе', error);
            }
        },
    }
}
</script>

<style scoped>
.login-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>