<template>
  <div class="topnav">
    <a href="#calulator" v-bind:style="{'background-color': navigation == 'CALCULATOR' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'CALCULATOR'">Calculator</a>
    <a href="#bookings" v-bind:style="{'background-color': navigation == 'BOOKINGS' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'BOOKINGS'">Bookings</a>
    <a href="#leads" v-bind:style="{'background-color': navigation == 'LEADS' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'LEADS'">Leads</a>
    <a href="/register" v-bind:style="{'background-color': navigation == 'REGISTER' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'REGISTER'">Register</a>
    <a href="/login" v-bind:style="{'background-color': navigation == 'LOGIN' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'LOGIN'">Login</a>
    <a href="#logout" v-bind:style="{'background-color': navigation == 'LOGOUT' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'LOGOUT'">Logout</a>
    <a href="#edit" v-bind:style="{'background-color': navigation == 'EDIT' ? '#11bfeb' : 'rgb(8, 8, 41)'}" @click="navigation = 'EDIT'">Edit</a>
  </div>
</template>

<script>
export default {
    name: "Navigation",
    data() {
      return {
        navigation: 'LOGIN'
      }
    }
};
</script>

<style>

/* Add a black background color to the top navigation */
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
  font-size: 14px;
  text-transform: uppercase;

}


</style>