import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuetify from "vuetify";
import 'vuetify/dist/vuetify.min.css'
import SignIn from "../components/SignIn";
import SignUp from "../components/SignUp";
import Case from "../components/Case";
import Jenkins from "../components/Jenkins";
import Task from "../components/Task";
import Report from "../components/Report";


// 防止路由冗余
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err=> err)
}


Vue.use(VueRouter)
Vue.use(Vuetify)

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/case',
    name: 'Case',
    component: Case
  },
  {
    path: '/task',
    name: 'Task',
    component: Task
  },
  {
    path: '/jenkins',
    name: 'Jenkins',
    component: Jenkins
  },
  {
    path: '/report',
    name: 'Report',
    component: Report
  }
]

const router = new VueRouter({
  routes
})
export default router
