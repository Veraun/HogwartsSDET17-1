import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from "./plugins/vuetify";
import api from './api/api'
import moment from "moment";
Vue.config.productionTip = false;
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
