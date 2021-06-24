import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from "./plugins/vuetify";
import api from './api/api'
import moment from "moment";
// 取消初运行的提示
Vue.config.productionTip = false;
// 将 api变量注册到 vue的变量池，其他使用vue实例的组件就可以拿到api使用
Vue.prototype.$api = api;

Vue.filter('dateFormat',(dataStr, pattern = 'YYYY-DD-MM HH:mm:ss') => {
  return moment(dataStr).format(pattern)
});

new Vue({
  el: '#app',
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app');
