<template>
    <div class="register-page">
        <form @submit.prevent="registerUser">
            <label>
                Логин:
                <input type="text" v-model="userData.username" required />
            </label>
            <br />
            <label>
                Email:
                <input type="email" v-model="userData.email" required />
            </label>
            <br />
            <label>
                Пароль:
                <input type="password" v-model="userData.password" required />
            </label>
            <br />
            <button type="submit">Зарегистрироваться</button>
        </form>
        <p>
            Уже есть аккаунт? <router-link to="/login">Войти.</router-link>
        </p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userData: {
                username: '',
                email: '',
                password: '',
            }
        }
    },
    methods: {
        async registerUSer() {
            try {
                //запрос к апи на регистрацию
                console.log('Регистрация', this.userData);
                alert('Регистрация успешна!');
                this.$router.push('/login'); //перенаправдление на логин
            } catch (error) {
                console.error('Ошибка регистрации', error);
                alert('Ошибка');
            }
        },
    }
}
</script>

<style>
div {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>