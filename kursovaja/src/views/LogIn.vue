<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Авторизация</h1>
        <div class="login-form text-center">
            <form @submit.prevent="login" class="form">
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

export default {
    data() {
        return {
            credentials: {
                username: '',
                password: '',
            },
            error: null,
        }
    },
    methods: {
        async login() {
            this.error = null;
            try {
                // Выполняем вход
                const response = await api.loginUser({
                    username: this.credentials.username,
                    password: this.credentials.password,
                });

                if (!response.data) {
                    throw new Error('Ответ от сервера пуст');
                }

                const { access, refresh } = response.data;

                if (!access || !refresh) {
                    throw new Error('Токены отсутствуют в ответе');
                }

                // Сохраняем токены в хранилище
                await this.$store.dispatch('setTokens', { access, refresh });

                // Получаем данные пользователя
                await this.$store.dispatch('fetchUser');

                console.log('Успешный вход:', response.data);
                this.$router.push('/profile');
            } catch (error) {
                console.error('Ошибка входа:', error);
                this.error = error.response?.data?.message || 'Неверный логин или пароль';
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