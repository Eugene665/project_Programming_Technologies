<template>
<router-link v-if="!isAuthenticated" to="/login" class="link">Вход/Регистрация</router-link>
<div v-else>Hello user <button @click="logout">Выйти</button></div>

</template>

<script>
import { ref, inject } from "vue";
export default {
    setup() {
      const login = inject('login');
      const isAuthenticated = inject('isAuthenticated');
      const logout = inject('logout');
      return {
        login,
        isAuthenticated,
        logout
      };
    }
}


</script>

