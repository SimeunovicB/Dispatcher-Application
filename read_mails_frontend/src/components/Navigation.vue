<template>
  <div class="topnav">
    <a href="#calulator">CALCULATOR</a>
    <a href="#about">BOOKINGS</a>
    <a class="leads" href="#contact">LEADS</a>
    <a href="#news">LOGOUT</a>
    <a class="active" href="#home">EDIT</a>
  </div>
</template>

<script>
export default {
    name: "Navigation"
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

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.leads {
  background-color: #11bfeb;
  color: white;
}

</style>