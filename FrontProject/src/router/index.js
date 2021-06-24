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
import Main from "../components/Main";
import TestCase from "../components/TestCase";

// 防止路由冗余
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err=> err)
};


Vue.use(VueRouter);
Vue.use(Vuetify);

const routes = [
  {
    path: '/login',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  // children 代表子路由，子路由加载前，会加载其父路由
  {
    path: '/main',
    name: 'Main',
    component: Main,
    children: [
      {
        path: '/report',
        name: 'Report',
        component: Report
      },
      {
        path: '/testcase',
        name: 'TestCase',
        component: TestCase
      }
    ]
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
  }

];

const router = new VueRouter({
  routes
});
export default router
