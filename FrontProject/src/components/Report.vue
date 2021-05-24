<template>
  <div>
    <template>
      <v-tabs :value="3" background-color="primary">
        <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
        <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
        <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
        <v-tab @click="$router.push({name:'Report'})">报告管理</v-tab>
      </v-tabs>
    </template>
    <div id="main" style="width: 500px;height: 500px;">

    </div>
  </div>
</template>

<script>
  export default {
    name: "Report",
    data(){
      return{

      }
    },
    methods:{

    },
    mounted() {
      var echarts = require('echarts');
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));
      // 绘制图表
      myChart.setOption({
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar',
          showBackground: true,
          backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
          }
        }]
      })
    }
  }
</script>

<style scoped>

</style>
