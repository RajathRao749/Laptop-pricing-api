<template>
  <div>
    <b-navbar toggleable="sm" type="dark" variant="dark" class="header">
      <b-navbar-brand>
        <router-link class="nav-heading" :to="{ path: '/' }">
          Retro Mailer
        </router-link>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse" />

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <b-nav-item>
              <router-link class="nav-item" :to="{ path: '/' }">
                Home
              </router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link class="nav-item" :to="{ path: '/login' }">
                Login
              </router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link class="nav-item" :to="{ path: '/register' }">
                Register
              </router-link>
            </b-nav-item>
          </b-navbar-nav>
          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              User
            </template>
            <b-dropdown-item>
              <router-link class="dropdown-router-item" :to="{ path: '/dashboard' }">
                Dashboard
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link class="dropdown-router-item" :to="{ path: '/' }">
                Logout
              </router-link>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>
    @media (min-width: 768px) {
        .header {
            padding: 1rem 16rem;
        }
    }
    .header {
        background-color: #222 !important;
    }
    .nav-heading {
        color: rgba(255,255,255,0.8) !important;
    }
    .nav-heading:hover {
        color: rgba(255,255,255,0.9) !important;
        text-decoration: none;
    }
    .nav-item {
        color: rgba(255,255,255,0.5) !important;
    }
    .nav-item:hover {
        color: rgba(255,255,255,0.8) !important;
        text-decoration: none;
    }
    .dropdown-router-item {
        color: #000 !important;
    }
    .dropdown-router-item:hover {
        text-decoration: none;      
    }
</style>
