import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/pages/Dashboard.vue'),
  },
  {
    path: '/new-expense',
    name: 'CreateExpense',
    component: () => import('@/pages/CreateNewExpense.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session?.isLoggedIn || false; // Ensure it is always defined

  try {
    await userResource.promise;
  } catch (error) {
    isLoggedIn = false;
  }

  if (!isLoggedIn) {
    window.location.href = "/login?redirect-to=/frontend";
  } else {
    next(); // Ensure next() is called if user is logged in
  }
});


// router.beforeEach(async (to, from, next) => {
//   let isLoggedIn = session.isLoggedIn
//   try {
//     await userResource.promise
//   } catch (error) {
//     isLoggedIn = false
//   }

//   if(!isLoggedIn){
//     window.location.href = "/login?redirect-to=/frontend"
//   }

  // if (to.name === 'Login' && isLoggedIn) {
  //   next({ name: 'Home' })
  // } else if (to.name !== 'Login' && !isLoggedIn) {
  //   next({ name: 'Login' })
  // } else {
  //   next()
  // }
// })

export default router
