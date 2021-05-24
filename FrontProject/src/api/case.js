import axios from "./http";

const cases = {
  getCaseList(params){
    return axios.get('/testCase/list', params)
  },
  createCaseByText(params){
    return axios.post('/testCase/text', params)
  },
  createCaseByFile(params){
    return axios.post('/testCase/text', params)
  }
}
export default cases;
