<template>
  <div class="login-page">
        <form @submit.prevent="loginUser">
            <label>
                Логин:
                <input type="text" v-model="userData.username" required />
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

}
</script>

<style>

</style>