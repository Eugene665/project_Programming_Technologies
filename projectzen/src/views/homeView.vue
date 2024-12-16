<template>
<router-link v-if="!isAuthenticated" to="/auth" class="link">Вход/Регистрация</router-link>
</template>
