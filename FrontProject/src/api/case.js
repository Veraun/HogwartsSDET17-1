import axios from "./http";

const cases = {
  getCaseList(){
    // return axios.get('/testCase/list', params)
    return axios.get('/testcase/get')
  },
  createCaseByText(params){
    return axios.post('/testCase/text', params)
  },
  createCaseByFile(params){
    return axios.post('/testCase/text', params)
  }
};
export default cases;
