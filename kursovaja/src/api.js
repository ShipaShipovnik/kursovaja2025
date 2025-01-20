import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
})

export default {
  // Получить список всех пользователей
  getUsers() {
    return apiClient.get('/users/');
  },
  // Получить список всех профилей
  getProfiles() {
    return apiClient.get('/profiles/');
  },
  // Зарегистрировать нового пользователя
  registerUser(userData) {
    return apiClient.post('/register/', userData);
  },
  // Авторизация
  loginUser(userData) {
    return apiClient.post('/login/', credentials);
  },
  //   Профиль поьзователя
  getUSerProfile() {
    return apiClient.get('/profile/');
  },
  //   данные конкретного профиля по айди
  getProfileDetail(profileId) {
    return apiClient.get(`/profiles/${profileId}/`);
  },
  //   обновление данных профиля
  updateProfile(profileId, profileData) {
    return apiClient.put(`/profiles/${profileId}/`, profileData);
  },
}
