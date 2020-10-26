<template>
  <div class="vue-template">
    <Header />
    <div class="container inner-block vertical-center">
      <form @submit.prevent="validate">
        <h3>Login</h3>

        <div class="form-group">
          <label>Email address</label>
          <input v-model="email" type="email" class="form-control form-control-lg">
          <label v-if="this.email.length > 40">Warning: Exceeded limit</label>
        </div>

        <div class="form-group">
          <label>Password</label>
          <input v-model="password" type="password" class="form-control form-control-lg">
          <label v-if="this.password.length > 20">Warning: Exceeded limit</label>
        </div>

        <button type="submit" class="btn btn-dark btn-lg btn-block">
          Sign In
        </button>

        <p class="forgot-password text-right mt-2 mb-4">
          <router-link to="/forgot-password">
            Forgot password?
          </router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Header from '../components/layout/Header.vue';

export default {
  name: 'Login',
  msg: '',
  components: {
    Header,
  },
  data() {
    return {
      email: '',
      password: '',
    };
  },

  methods: {
    validate() {
      if (this.email.length < 2 || this.email.length > 40) {
        alert('Email length < 2 or > 20');
      } 
      else if (this.password.length < 2 || this.password.length > 20) {
        alert('Password length < 2 or > 40');
      } 
      else {
        this.handleSubmit();
      }
    },
    handleSubmit() {
      const data = {
        email: this.email,
        password: this.password,
      };
      console.log(data);
      axios.post('http://localhost:5000/login', data)
        .then((response) => {
          console.log(response);
          if (response.data === 'Invalid Credentials') {
            alert('Invalid Credentials - Login agian');
            this.$router.replace('/login');
          } else {
            alert('Login Successfull');
            this.$router.replace('/');
          }
        })
        .catch((error) => {
          console.log(error);
          alert('Invalid Credentials - Login agian');
        });
    },
  },
};
</script>

<style scoped>
  .container {
    margin-top: 4rem;
  }
</style>
