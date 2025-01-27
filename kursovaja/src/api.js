import axios from 'axios'
import store from './store';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
})

// Добавляем токен в заголовки запросов
apiClient.interceptors.request.use((config) => {
  const token = store.state.accessToken;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

apiClient.interceptors.response.use(
  (response) => response, // Успешный ответ
  async (error) => {
    if (error.response) {
      // Ошибка 401 (неавторизован)
      if (error.response.status === 401) {
        // Попробуем обновить токен
        const refreshToken = localStorage.getItem('refreshToken')
        if (refreshToken) {
          try {
            const response = await apiClient.post('/token/refresh/', {
              refresh: refreshToken,
            })
            const newAccessToken = response.data.access
            localStorage.setItem('accessToken', newAccessToken)

            // Повторяем оригинальный запрос с новым токеном
            error.config.headers.Authorization = `Bearer ${newAccessToken}`
            return apiClient(error.config)
          } catch (refreshError) {
            // Если обновление токена не удалось, перенаправляем на страницу входа
            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')
            window.location.href = '/login'
          }
        } else {
          // Если refresh-токена нет, перенаправляем на страницу входа
          window.location.href = '/login'
        }
      }
      console.error('Ошибка API:', error.response.data)
    } else if (error.request) {
      // Ошибка сети (запрос был отправлен, но ответ не получен)
      console.error('Ошибка сети:', error.request)
    } else {
      // Другие ошибки
      console.error('Ошибка:', error.message)
    }
    return Promise.reject(error)
  },
)

export default {
  // токены итд
  loginUser(credentials) {
    return apiClient.post('/token/', credentials)
  },
  verifyToken(token) {
    return apiClient.post('/token/verify/', { token })
  },
  refreshToken(refreshToken) {
    return apiClient.post('/token/refresh/', { refresh: refreshToken })
  },
  // Зарегистрировать нового пользователя
  registerUser(userData) {
    return apiClient.post('/users/register/', userData)
  },
  // Юзеры
  getUsers() {
    return apiClient.get('/users/')
  },
  getCurrentUser() {
    return apiClient.get('/my-user/')
  },
  // Профили
  getProfiles() {
    return apiClient.get('/users/profiles/')
  },
  getCurrentProfile() {
    return apiClient.get('/my-profile/')
  },
  getProfileDetail(profileId) {
    return apiClient.get(`/profile/${profileId}/`)
  },
  updateProfile(profileId, profileData) {
    return apiClient.put(`/profile/${profileId}/`, profileData)
  },
  // Категории
  getCategories() {
    return apiClient.get('/services/categories-list/')
  },
  // Усуги
  createService(formData) {
    return apiClient.post('/services/create/', formData)
  },
  getServices(){
    return apiClient.get('/services/services-list/')
  },
  getMyServices(){
    return apiClient.get('/services/my-services/')
  }
}
