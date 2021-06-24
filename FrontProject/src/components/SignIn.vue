<template>
  <v-main>
    <div class="login-form">
      <h1>登录</h1>
      <v-text-field label="用户名" v-model="username" outlined clearable></v-text-field>
      <v-text-field label="密码" type="password" v-model="password" outlined clearable></v-text-field>

      <v-btn color="primary" @click="login()">登录</v-btn>
      <v-btn color="primary" text @click="signUp()">注册</v-btn>

    </div>
  </v-main>
</template>

<script>
  export default {
    // data 在vue代表定义数据
    // data是函数，因为vue中代表实例变量
    data(){
      return{
        username:'',
        password:''
      }
    },
    methods: {
      signUp() {
        console.log('123')
        // 实现跳转
        // this.$router.push :把一个路由推入栈
        this.$router.push({name: 'SignUp'})
      },
      login() {
        // let 代表定义变量
        let loginData = {
          username: this.username,
          password: this.password
        };
        console.log(loginData);
        // 使用vue实例中注册的api变量
        // .then 是axios回调方法 => 获取返回结果
        // => 函数：ES6，定义一个匿名函数，使用当前环境
        this.$api.user.login(loginData).then(res => {
          console.log(res);
          // 调登录接口成功后，存token
          if (res.status == 200) {
            // localStorage 是存储到浏览器中的一个数据，全局可用
            localStorage.setItem('token', res.data.access_token);

            // 登录成功后，跳转到默认页面：TestCase页面
            this.$router.push({name:'TestCase'})
          }
        });
      }
    }

  }
</script>

<style scoped>
  .login-form{
    /*设置长度*/
    width: 500px;
    /*将整个标签居中*/
    margin: 0 auto;
    /*将文本和按钮居中*/
    text-align: center;
  }
</style>
