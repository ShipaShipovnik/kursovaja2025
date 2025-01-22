import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  withCredentials: true,
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
    return apiClient.get('/users/profiles/');
  },
  // Зарегистрировать нового пользователя
  registerUser(userData) {
    return apiClient.post('/users/register/', userData);
  },
  // Авторизация
  loginUser(credentials) {
    return apiClient.post('/users/login/', credentials);
  },
  checkAuth() {
    return apiClient.get('/users/check-auth/');
  },
  //   Профиль поьзователя
  getUserProfile() {
    return apiClient.get('/users/profile/');
  },
  //   данные конкретного профиля по айди
  getProfileDetail(profileId) {
    return apiClient.get(`/users/profiles/${profileId}/`);
  },
  //   обновление данных профиля
  updateProfile(profileId, profileData) {
    return apiClient.put(`/users/profiles/${profileId}/`, profileData);
  },
}
