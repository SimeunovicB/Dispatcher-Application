<template>
  <div id="app">
    <div class="topnav">
      <router-link
        to="#calculator"
        v-bind:style="{
          'background-color':
            navigation == 'CALCULATOR' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'CALCULATOR'"
        >Calculator</router-link
      >
      <router-link
        to="#bookings"
        v-bind:style="{
          'background-color':
            navigation == 'BOOKINGS' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'BOOKINGS'"
        >Bookings</router-link
      >
      <router-link
        v-if="loggedIn"
        to="/leads"
        v-bind:style="{
          'background-color':
            navigation == 'LEADS' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'LEADS'"
        >Leads</router-link
      >
      <router-link
        to="#edit"
        v-bind:style="{
          'background-color':
            navigation == 'EDIT' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'EDIT'"
        >Edit</router-link
      >
      <router-link
        v-if="loggedIn"
        to=""
        v-bind:style="{
          'background-color':
            navigation == 'LOGOUT' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="logout()"
        >Logout</router-link
      >
      <router-link
        v-if="!loggedIn"
        to="/"
        v-bind:style="{
          'background-color':
            navigation == 'LOGIN' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'LOGIN'"
        >Login</router-link
      >
      <router-link
        v-if="!loggedIn"
        to="/register"
        v-bind:style="{
          'background-color':
            navigation == 'REGISTER' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'REGISTER'"
        >Register</router-link
      >
      <router-link
        v-if="isAdmin"
        to="/users"
        v-bind:style="{
          'background-color':
            navigation == 'USERS' ? '#297b99' : 'rgb(8, 8, 41)',
        }"
        @click="navigation = 'USERS'"
        >Users</router-link
      >
    </div>

    <div class="card">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {}, //Navigation, } // Pagination, LeadsTypeAndSearch, DateAndPriority, Leads },
  data() {
    return {
      navigation: "",
      auth: false,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.authenticated;
    },
    isAdmin() {
      return this.$store.state.administrator;
    },
  },
  async mounted() {
    await fetch("http://127.0.0.1:8000/api/read/mail", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    });

    try {
      const response = await fetch("http://127.0.0.1:8000/api/user", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      // response.json().then(result => console.log(result))

      const content = await response.json();
      console.log(content);
      if (response.status == 200) {
        this.$store.dispatch("setAuth", true);
        if (content.is_superuser) {
          this.$store.dispatch("setAdmin", true);
        } else {
          this.$store.dispatch("setAdmin", false);
        }
      } else {
        this.$store.dispatch("setAuth", false);
        this.$store.dispatch("setAdmin", false);
      }
    } catch (e) {
      await this.$store.dispatch("setAuth", false);
      await this.$store.dispatch("setAdmin", false);
    }

    // setInterval(function(){ alert("Hello"); }, 3000);

    // var that = this;
    // setInterval(async function () {
    //   const response = await fetch("http://127.0.0.1:8000/api/leads", {
    //     method: "GET",
    //     headers: { "Content-Type": "application/json" },
    //     credentials: "include",
    //   });
    //   console.log("poziv")
    //   const leads = await response.json();
    //   console.log(leads)
    //   // const le = [1,2,3,4]
    //   const le = "aj"
    //   that.$store.dispatch("setLeads", leads);
    // }, 3000);
  },
  methods: {
    async logout() {
      await fetch("http://127.0.0.1:8000/api/logout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      })
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            this.$router.replace("/");
            this.$store.dispatch("setAuth", false);
            this.$store.dispatch("setAdmin", false);
          }
        })
        .catch((error) => {
          console.log(error);
          this.errorMessage = error;
        });
    },

    deliAuth() {
      this.auth = this.$store.state.authenticated;
    },
  },
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
  /* box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2); */
  margin-left: auto;
  margin-right: auto;
}
</style>
