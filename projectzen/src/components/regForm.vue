<template>
    <div>
      <h2>Зарегистрироваться</h2>
      <form @submit.prevent="signUp">
        <input v-model="username" type="text" placeholder="Ваш логин" required />
        <input v-model="email" type="email" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Пароль" required />
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>


<script>
  import { inject } from 'vue';
  import { signup } from '../lib/common_methods';
  
  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    setup() {
      const login = inject('login');
      return {
        login
      };
    },
    methods: {
      async signUp() {
        try {
          await signup(this.email, this.password, this.username);

          //this.login({ email: this.email, username: this.username });
          this.$router.push('/');
        } catch (error) {
          alert(error.message);
        }
      }
    }
  };
  </script>
  