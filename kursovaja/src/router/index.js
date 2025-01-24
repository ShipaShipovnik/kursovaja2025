import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Register from '@/views/Register.vue'
import LogIn from '@/views/LogIn.vue'
import Search from '@/views/Search.vue'
import FAQ from '@/views/FAQ.vue'
import Profile from '@/views/Profile.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn,
  },
  {
    path: '/logout',
    name: 'LogOut',
    component: LogIn,
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
  },
  {
    path: '/faqs',
    name: 'FAQs',
    component: FAQ,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
]

const router = createRouter({ history: createWebHistory(), routes })

export default router;
