<template>
    <div class="main-block register-page container shadow p-5">
        <h1 class="h1 text-center">Регистрация</h1>
        <div class="register-form form text-center">
            <form @submit.prevent="registerUser" class="form">
                <label class="form-label">
                    Логин:
                    <input class="form-control" type="text" v-model="userData.username" required />
                </label>
                <br />
                <label class="form-label">
                    Email:
                    <input class="form-control" type="email" v-model="userData.email" required />
                </label>
                <br />
                <label class="form-label">
                    Пароль:
                    <input class="form-control" type="password" v-model="userData.password" required />
                </label>
                <br />
                <label class="form-label">
                    Возраст:
                    <input class="form-control" type="number" v-model="userData.age" required />
                </label>
                <br />
                <button type="submit " class="btn btn-warning">Зарегистрироваться</button>
            </form>
            <p class="mt-4 text-muted">
                Уже есть аккаунт? <router-link to="/login" class="text-warning">Войти.</router-link>
            </p>
        </div>
    </div>

</template>

<script>
import api from '@/api';

export default {
    data() {
        return {
            userData: {
                username: '',
                email: '',
                password: '',
                age: '',
            }
        }
    },
    methods: {
        async registerUser() {
            if (!this.userData.username || !this.userData.email || !this.userData.password || !this.userData.age) {
                alert('Пожалуйста, заполните все поля.');
                return;
            }

            if (this.userData.password.length < 8) {
                alert('Пароль должен содержать не менее 8 символов.');
                return;
            }

            try {
                const response = await api.registerUser(this.userData);
                console.log('Регистрация успешна:', response.data);

                // Сохраняем данные пользователя в Vuex (если используется)
                this.$store.dispatch('setUser', response.data.user);

                alert('Регистрация успешна!');
                this.$router.push('/profile'); // Перенаправление на страницу профиля
            } catch (error) {
                console.error('Ошибка регистрации:', error.response?.data);

                // Вывод сообщения об ошибке пользователю
                if (error.response?.data?.detail) {
                    alert(`Ошибка: ${error.response.data.detail}`);
                } else {
                    alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
                }
            }
        },
    }
}
</script>

<style scoped>
.register-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>