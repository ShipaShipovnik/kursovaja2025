<script setup>
import Header from './components/Header.vue';
// import { ref, onMounted } from 'vue';
// import api from './api';

// const user = ref({
//   id: null,
//   username: '',
//   email: '',
//   profile: {
//     profileName: '',
//     profileDescr: '',
//     spec: '',
//   },
// })

// const serviceList = ref({
//   // 
// })

// //Регистрация
// const loadUserProfile = async () => {
//   try {
//     const response = await api.getUSerProfile();
//     const data = response.data;
//     user.value = {
//       id: data.id,
//       username: data.username,
//       email: data.email,
//       profile: {
//         profileName: data.profile ? data.profile.profileName : 'Новый Профиль',
//         profileDescr: data.profile ? data.profile.profileDescr : 'Описание отсутствует',
//         spec: data.profile ? data.profile.spec : '-',
//       }
//     };
//   } catch (error) {
//     console.error('Ошибка загрузки данных профиля пользователя', error)
//   }
// };
// //Загрузка данных оп профиле



</script>

<template>
  <div class="wrapper">
    <Header />
    <router-view>
    </router-view>

    <!-- <div class="profile-layout">
      <div class="container pt-5 row mx-auto h-75">
        <div class="sidebar col-4  w-25 p-3 mx-auto shadow-lg">
          <div class="container">
            <img src="https://sh122-omsk-r52.gosweb.gosuslugi.ru/netcat_files/9/67/team_fpo_woman_1100x1100_4.png"
              alt="" class="avatar mb-3 img-fluid">
            <h4 class="card-title mb-1">{{ user.profileName }}</h4>
            <p>{{ user.spec }}</p>
            <div class="tab-btns">
              <a href class="btn mb-2 d-block btn-warning">Главная</a>
              <a href class="btn mb-2 d-block btn-warning">Галерея</a>
              <a href class="btn d-block btn-warning">FAQs</a>
            </div>
            <div class="socials">
              <a href=""><svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor"
                  class="bi bi-telegram" viewBox="0 0 16 16">
                  <path
                    d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.287 5.906q-1.168.486-4.666 2.01-.567.225-.595.442c-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294q.39.01.868-.32 3.269-2.206 3.374-2.23c.05-.012.12-.026.166.016s.042.12.037.141c-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8 8 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629q.14.092.27.187c.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.4 1.4 0 0 0-.013-.315.34.34 0 0 0-.114-.217.53.53 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09" />
                </svg></a>
            </div>
          </div>
        </div>
        <div class="col-1"></div>
        <div class="main-block p-3 col shadow-lg">
          <div class="container">
            <div class="services-list">
              <div class="card mb-3 service-card" v-for="service in serviceList" :key="id">
                <div class="row g-0 p-2">
                  <div class="col">
                    <div class="service-img"><img src="" alt="фото услуги"></div>
                  </div>
                  <div class="col-md-8">
                    <div class="card-body">
                      <h5 class="card-title">{{ service.title }}</h5>
                      <p class="card-text">
                        {{ service.descr }}
                      </p>
                      <p class="card-text d-flex align-items-end justify-content-between">
                        <small class="text-muted align-middle">Срок {{ service.workTime }}</small>
                        <a class="btn btn-warning">{{ service.priceMin }} р - {{ service.priceMax }} р.</a>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div> -->
    <!-- 
                        <div class="about-text">
                            <p>
                                Lorem ipsum dolor sit, amet consectetur
                                adipisicing elit.
                                Quibusdam est eius architecto quas blanditiis
                                quasi odio
                                praesentium aspernatur cum accusantium provident
                                excepturi
                                eaque, quidem ducimus similique repudiandae
                                error incidunt iste?
                            </p>
                            <p>
                                Lorem ipsum dolor sit, amet consectetur
                                adipisicing elit.
                                Quibusdam est eius architecto quas blanditiis
                                quasi odio
                                praesentium aspernatur cum accusantium provident
                                excepturi
                                eaque, quidem ducimus similique repudiandae
                                error incidunt iste?
                            </p>
                        </div>
                        <div class="about-links">
                            <li class="list-group-item">
                                <span class="text-secondary">ВКонтакте:</span>
                                <a href class="primary-link">укпуцкпукпукп</a>
                            </li>
                            <li class="list-group-item">
                                <span class="text-secondary">ТГ:</span>
                                <a href class="primary-link">кпакупук</a>
                            </li>
                        </div> -->
    <!-- </div>
  </div>
  </div>
  </div> -->
  </div>
</template>

<style scoped>
.wrapper {
  font-family: Arial, sans-serif;
}
</style>
