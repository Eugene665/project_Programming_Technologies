<template>
        <nav>
      <router-link to="/" exact>Главная</router-link> <br>
      <router-link to="/auth" active-class="active-link">Вход/Регистрация</router-link>
    </nav>
    <div>
      <LoginForm />
      <SignupForm />
    </div>
  </template>
  
  <script>
  import LoginForm from '../components/logForm.vue';
  import SignupForm from '../components/regForm.vue';
  
  export default {
    components: {
      LoginForm,
      SignupForm
    }
  };
  </script>
  