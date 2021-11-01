<template>
  <div id="app">

    <!-- <Navigation /> -->
    <!-- <div class="card">
      <Pagination/>
      <LeadsTypeAndSearch/>
      <date-and-priority/>
      <leads/>
    </div> -->

    <div class="topnav">
      <router-link to="#calculator" v-bind:style="{'background-color': navigation == 'CALCULATOR' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'CALCULATOR'">Calculator</router-link>
      <router-link to="#bookings" v-bind:style="{'background-color': navigation == 'BOOKINGS' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'BOOKINGS'">Bookings</router-link>
      <router-link to="/leads" v-bind:style="{'background-color': navigation == 'LEADS' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'LEADS'">Leads</router-link>
      <router-link to="#edit" v-bind:style="{'background-color': navigation == 'EDIT' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'EDIT'">Edit</router-link>
      <router-link v-if="loggedIn" to="" v-bind:style="{'background-color': navigation == 'LOGOUT' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="logout()">Logout</router-link>
      <router-link v-if="!loggedIn" to="/login" v-bind:style="{'background-color': navigation == 'LOGIN' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'LOGIN'">Login</router-link>
      <router-link  v-if="!loggedIn" to="/register" v-bind:style="{'background-color': navigation == 'REGISTER' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'REGISTER'">Register</router-link>
    </div>

    <div class="card">
      <router-view/>
    </div>
  </div>
</template>

<script>
// import DateAndPriority from './components/DateAndPriority.vue';
// import Leads from './components/Leads.vue';
// import LeadsTypeAndSearch from './components/LeadsTypeAndSearch.vue';
// import Pagination from './components/Pagination.vue';
// import Proba from './components/Proba.vue';
// import Navigation from "./components/Navigation.vue";
// import {computed} from 'vue';
export default {
  name: "App",
  components: {}, //Navigation, } // Pagination, LeadsTypeAndSearch, DateAndPriority, Leads },
  data() {
    return {
      navigation: "LOGIN",
      // auth: computed(this.$store.state.authenticated)
      auth: false
      
    }
  },
  computed: {
    loggedIn() {
        return this.$store.state.authenticated;
      },
  },
  mounted() {
    console.log("ae")
    // this.auth = this.$store.state.authenticated;
  },
  methods: {
  //   async logout () {
  //   console.log("IDE MO MO MO");
  //   await fetch("http://127.0.0.1:8000/api/logout", {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     credentials: "include",
  //   });

  // },

  async logout() {
      await fetch("http://127.0.0.1:8000/api/logout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      }).then((response) => {
        console.log(response);
        if(response.status == 200) {
          this.$router.replace("/login");
          this.$store.dispatch('setAuth', false);
        }
      }).catch(error => {
        console.log(error);
        this.errorMessage = error;
      });
    },

  deliAuth() {
    this.auth = this.$store.state.authenticated;
  }
  }
};
</script>

<style>
html {
  background-color: rgb(245, 245, 245);
}

.topnav {
  background-color: rgb(8, 8, 41);
  overflow: hidden;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  display: flex;
  flex-direction: row-reverse;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: right;
  color: #f2f2f2;
  text-align: center;
  padding: 12px 16px;
  text-decoration: none;
  font-size: 16px;
  text-transform: uppercase;

}

.topnav router-link {
  float: right;
  color: #f2f2f2;
  text-align: center;
  padding: 12px 16px;
  text-decoration: none;
  font-size: 16apx;
  text-transform: uppercase;

}

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: arial;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
}

.card {
  background-color: rgb(245, 245, 245);
  border-radius: 6px;
  width: 80%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  margin-left: auto;
  margin-right: auto;
}




</style>
