<template>
    <div>
        <p>Вы уверены, что хотите выйти?</p>
        <button @click="logout">Выйти</button>
    </div>
</template>

<script>
import api from '@/api';

export default {
    
    methods: {
        async logout() {
            try {
                await api.logoutUser();
                this.$root.isAuthenticated = false;
                this.$root.username = '';
                this.$router.push('/login');
            } catch (error) {
                console.error('Ошибка при выходе', error);
            }
        },
    }
}
</script>

<style></style>