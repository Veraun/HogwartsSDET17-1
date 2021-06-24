import axios from "axios";
import router from "../router/index";
// 创建 axios 的实例
var instance = axios.create({
  // 头信息
  headers: {
    'Content-Type': 'application/json'
  },
  // 超时时间
  timeout: 10000,
  // 基础url
  // baseURL:'http://stuq.ceshiren.com:8089'
  baseURL: 'http://localhost:5000'
});


// 发送请求的拦截器：在发送请求前会主动的调用此函数
// 如果本地的localStorage存了token这个字段，那么就把token存到发送请求的header中
instance.interceptors.request.use(function (config) {
  // 如果 token存在 且 发送的请求不是登录接口的话，就把token加入到认证中
  if (localStorage.getItem('token') && config.url != "/login") {
    config.auth = {username: localStorage.getItem('token'), password: ""}
  }
  return config;
});

// 如果发送的请求，响应的信息内有错误，会回调 error 中的内容
instance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // 如果请求结果状态码是 401 的话，代表校验失败
    // 此时需要跳转到登陆界面，同时清理 token
    if (error.response) {
      if (error.response.status == 401) {
        console.log("执行到这了。。。");
        // 清除 token
        localStorage.removeItem("token");
        // 替换最上层路由的页面
        router.replace({ name: "SignIn" });
        // 拒绝请求
        return Promise.reject(error);
      }
    }
  }
);

// 导出实例
export default instance
