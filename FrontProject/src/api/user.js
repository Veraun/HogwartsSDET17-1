import axios from "./http";

const user = {
  login(loginData){
    // auth代表校验
    return axios.get("/login", {auth: loginData})
  },
  // signIn(params){
  //   return axios.post('/user/login', params)
  // },
  signUp(params){
    return axios.post('/user/register', params)
  }
};
export default user
