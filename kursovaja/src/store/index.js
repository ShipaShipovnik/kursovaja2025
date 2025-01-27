import axios from 'axios'
import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    profile: null,
    isAuthenticated: false,
    accessToken: localStorage.getItem('accessToken') || null, // Восстанавливаем токен из localStorage
    refreshToken: localStorage.getItem('refreshToken') || null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user
    },
    SET_PROFILE(state, profile) {
      state.profile = profile
    },
    SET_AUTHENTICATED(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated
    },
    SET_TOKENS(state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
      state.isAuthenticated = !!access

      // Сохраняем токены в localStorage
      localStorage.setItem('accessToken', access)
      localStorage.setItem('refreshToken', refresh)
    },
    CLEAR_TOKENS(state) {
      state.accessToken = null
      state.refreshToken = null
      state.isAuthenticated = false
      state.user = null

      // Удаляем токены из localStorage
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
    },
  },
  actions: {
    // Установка токенов после успешного входа
    setTokens({ commit }, { access, refresh }) {
      commit('SET_TOKENS', { access, refresh })
    },

    // Вход пользователя
    async login({ dispatch }, credentials) {
      try {
        const response = await axios.post('/api/token/', credentials)
        const { access, refresh } = response.data
        dispatch('setTokens', { access, refresh })
        await dispatch('fetchUser')
      } catch (error) {
        console.error('Ошибка входа:', error)
        throw error
      }
    },

    // Выход пользователя
    logout({ commit }) {
      commit('CLEAR_TOKENS')
    },

    async fetchUser({ commit, state }) {
      try {
        // Получаем данные пользователя
        const response = await axios.get('http://127.0.0.1:8000/api/users/my-user/', {
          headers: {
            Authorization: `Bearer ${state.accessToken}`,
          },
        })
        // Получаем данные его профиля
        const profileResponse = await axios.get('http://127.0.0.1:8000/api/users/my-profile/', {
          headers: {
            Authorization: `Bearer ${state.accessToken}`,
          },
        })

        console.log('Данные пользователя:', response.data) // Логируем данные
        console.log('Данные профиля:', profileResponse.data) // Логируем данные
        commit('SET_USER', response.data)
        commit('SET_PROFILE', profileResponse.data)
        commit('SET_AUTHENTICATED', true)
      } catch (error) {
        console.error('Ошибка при получении данных:', error)
        commit('SET_AUTHENTICATED', false)
        commit('SET_USER', null)
        commit('SET_PROFILE', null)
      }
    },

    // Обновление токена
    async refreshToken({ commit, state }) {
      try {
        const response = await axios.post('/api/token/refresh/', {
          refresh: state.refreshToken,
        })
        const { access } = response.data
        commit('SET_TOKENS', { access, refresh: state.refreshToken })
        return access
      } catch (error) {
        console.error('Ошибка при обновлении токена:', error)
        commit('CLEAR_TOKENS')
        throw error
      }
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    user: (state) => state.user,
    profile: (state) => state.profile,
    accessToken: (state) => state.accessToken,
    refreshToken: (state) => state.refreshToken,
  },
})
