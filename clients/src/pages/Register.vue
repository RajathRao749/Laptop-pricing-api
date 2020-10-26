<template>
  <div class="vue-template">
    <Header />
    <div class="container inner-block vertical-center">
      <form @submit.prevent="validate">
        <h3>Register</h3>

        <div class="form-group">
          <label>Company Name</label>
          <input v-model="companyname" type="text" class="form-control form-control-lg">
          <label v-if="this.companyname.length > 20">Warning: Exceeded limit</label>
        </div>

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

         <div class="form-group">
           <label>Region</label>
          <select v-model="selected" multiple>
            <option>A</option>
            <option>B</option>
            <option>C</option>
          </select>
           <br>
            <span>Selected: {{ selected }}</span>
          </div>

          <div class="form-group">
           <label>Industry</label>
          <select v-model="selected" multiple>
            <option>A</option>
            <option>B</option>
            <option>C</option>
            <option>D</option>
          </select>
           <br>
            <span>Selected: {{ selected }}</span>
          </div>

        <button type="submit" class="btn btn-dark btn-lg btn-block">
          Register
        </button>
        </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Header from '../components/layout/Header.vue';

export default {
  name: 'Register',
  components: {
    Header,
  },
  data() {
    return {
      companyname: '',
      email: '',
      password: '',
      selected:'',
    };
  },
  methods: {
    validate() {
      if (this.email.length < 2 || this.email.length > 40) {
        alert('Email length < 2 or > 20');
      } 
      else if (this.password.length < 2 || this.password.length > 20) {
        alert('Password length < 2 or > 20');
      } 
      else if (this.companyname.length < 2 || this.companyname.length > 20) {
        alert('Username length < 2 or > 20');
      }  
      else {
        this.handleSubmit();
      }
    },
    handleSubmit() {
      const data = {
        companyname: this.companyname,
        email: this.email,
        password: this.password,
        selected: this.selected,
      };
      axios.post('http://localhost:5000/register', data)
        .then((response) => console.log(response))
        .catch((err) => console.log(err));
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
  .container {
    margin-top: 0.5 rem;
  }
</style>
