<template>
    <div>
      <h2>Зарегистрироваться</h2>
      <form @submit.prevent="signUp">
        <input type="radio" name="isUser" @click="radioChoice = true;" id="Company"> <label for="Company">Компания</label>
        <input type="radio" name="isUser" @click="radioChoice = false;" id="User" checked><label for="User">Пользователь</label>
        <input v-model="username" type="text" placeholder="Ваш логин" required />
        <input v-model="email" type="email" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Пароль" required />
        <textarea v-if="radioChoice" v-model="about" placeholder="Расскажите о вашей компании"></textarea>
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>


<script>
  import { inject, ref } from 'vue';
  import { signup } from '../lib/common_methods';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        about: ''
      };
    },
    setup() {
      const login = inject('login');
      const radioChoice = ref(false);
      return {
        login,
        radioChoice
      };
    },
    methods: {
      async signUp() {
        try {
          await signup(this.email, this.password, this.username, this.radioChoice, this.about);

          this.login({ email: this.email, username: this.username });
          this.$router.push('/');
        } catch (error) {
          alert(error.message);
        }
      }
    }
  };
  </script>
  