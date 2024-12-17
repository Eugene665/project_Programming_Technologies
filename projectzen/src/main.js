import { createApp, ref } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

const isAuthenticated = ref(false);
const user = ref({});

const login = (userData) => {
  isAuthenticated.value = true;
  user.value = userData;
  localStorage.setItem("userLogin", JSON.stringify(userData));
};

const logout = () => {
  isAuthenticated.value = false;
  user.value = {};
  localStorage.removeItem("userLogin");
  router.push("/login");
};

app.provide("isAuthenticated", isAuthenticated);
app.provide("user", user);
app.provide("logout", logout);
app.provide("login", login);

app.use(router);
app.mount("#app");

const uid = localStorage.getItem("userLogin");
if (uid) {
  const userData = JSON.parse(uid);
  console.log(userData);
  isAuthenticated.value = true;
  user.value = userData;
} else {
  isAuthenticated.value = false;
}
