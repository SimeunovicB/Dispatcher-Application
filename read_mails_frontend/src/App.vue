<template>
  <div id="app">
    <!-- <div class="topnav">
      <a href="#calulator">CALCULATOR</a>
      <a href="#about">BOOKINGS</a>
      <a class="leads" href="#contact">LEADS</a>
      <a href="#news">LOGOUT</a>
      <a class="active" href="#home">EDIT</a>
    </div> -->
    <Navigation />
    <div class="card">
      <Pagination/>
      <LeadsTypeAndSearch/>
      <date-and-priority/>
      <leads/>
      <!-- <Proba/> -->
    </div>
  </div>
</template>

<script>
import DateAndPriority from './components/DateAndPriority.vue';
import Leads from './components/Leads.vue';
import LeadsTypeAndSearch from './components/LeadsTypeAndSearch.vue';
import Navigation from "./components/Navigation.vue";
import Pagination from './components/Pagination.vue';
// import Proba from './components/Proba.vue';
export default {
  name: "App",
  components: { Navigation, Pagination, LeadsTypeAndSearch, DateAndPriority, Leads },
};
</script>

<style>
html {
  background-color: rgb(245, 245, 245);
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
  /* display: flex; */
  /* flex-direction: row; */
  margin-left: auto;
  margin-right: auto;
  /* justify-content: flex-start; */
  /* align-items: flex-start; */
}




</style>
