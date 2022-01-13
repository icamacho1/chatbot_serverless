import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    { path: '/', name: "Home", component: () => import('../views/Home.vue')},
    { path: '/chatbot/:cookie', name: "Home2", component: () => import('../views/Home2.vue')}
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
