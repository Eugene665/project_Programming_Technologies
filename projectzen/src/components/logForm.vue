<template>
    <div>
      <h2>Вход</h2>
      <form @submit.prevent="login">
        <input v-model="email" type="text" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Пароль" required />
        <button type="submit">Войти</button>
        <router-link to="/register">Нет аккаунта? Зарегистрироваться</router-link>
      </form>
    </div>
  </template>
  
  <script>
  import { inject } from 'vue';
  import { authenticateUser } from '../lib/common_methods';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
        username: '',
      };
    },
    setup() {
      const login = inject('login');
      return {
        login
      };
    },
    methods: {
      async login() {
        try {
          const usr = await authenticateUser(this.email, this.password);
          
          this.login({ email: usr.email, id: usr.id, username: usr.username, icon: usr.profile_icon_path });
          this.$router.push('/');
        } catch (error) {
          alert(error.message);
        }
      }
    }
  };
  </script>
  