import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

const accessToken = localStorage.getItem('accessToken')
if (accessToken) {
  store.dispatch('fetchUser') // Загружаем данные пользователя
}

const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
