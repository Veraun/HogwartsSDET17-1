import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from "./plugins/vuetify";
import api from './api/api'
Vue.config.productionTip = false
Vue.prototype.$api = api

new Vue({
  el: '#app',
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app')
