import axios from "axios";
var instance = axios.create({
  headers: {
    'Content-Type':'application/json'
  },
  baseURL:'http://stuq.ceshiren.com:8089'
});


// 发送请求的拦截器
// 如果本地的localStorage存了token这个字段，那么就把token存到发送请求的header中
instance.interceptors.request.use(config=>{
  if(localStorage.getItem('token')){
    config.headers.common['token'] = localStorage.getItem('token')
  }
  return config
});


export default instance
