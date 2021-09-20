import axios from "~/helpers/axios";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
  login(username, password) {
    return post("/api/login", { username: username, password: password });
  },
  logout() {
    return post("/api/logout");
  },
  whoami() {
    return get("/api/whoami");
  },
  list_tweets(username) {
    return get("/api/list_tweets", { username });
  },
  get_user_details(username) {
    return get("/api/get_user_details", { username });
  },
  toggle_follow(username, value) {
    console.log(value)
    return post("/api/toggle_follow", { username, value });
  },
  tweet(content) {
    return post("/api/tweet", { content });
  }
};
export default api;

function get(url, params) {
  return axios.get(url, { params: params });
}

function post(url, params) {
  var fd = new FormData();
  params = params || {};
  Object.keys(params).map(k => {
    fd.append(k, params[k]);
  });
  return axios.post(url, fd);
}
