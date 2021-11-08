<template>
  <div class="typesAndSearch">
    <div class="types">
      <button
        class="btn"
        v-bind:style="{
          'background-color': activeBtn == 'TARGET LEADS' ? '#297b99' : 'white',
          'color': activeBtn == 'TARGET LEADS' ? 'white' : 'black',
        }"
        @click="buttonOne()"
      >
        Target Leads
      </button>
      <button
        class="btn"
        v-bind:style="{
          'background-color': activeBtn == 'ALL LEADS' ? '#297b99' : 'white',
          'color': activeBtn == 'ALL LEADS' ? 'white' : 'black',
        }"
        @click="buttonTwo()"
      >
        All leads
      </button>
      <button
        class="btn"
        v-bind:style="{
          'background-color': activeBtn == 'MY LEADS' ? '#297b99' : 'white',
          'color': activeBtn == 'MY LEADS' ? 'white' : 'black',
        }"
        @click="buttonThree()"
      >
        My leads
      </button>
      <button
        class="btn"
        v-bind:style="{
          'background-color': activeBtn == 'SORT BY SHIPPING DATE' ? '#297b99' : 'white',
          'color': activeBtn == 'SORT BY SHIPPING DATE' ? 'white' : 'black',
        }"
        @click="buttonFour()"
      >
        Sort by shipping date
      </button>
      <button
        class="btn"
        v-bind:style="{
          'background-color': activeBtn == 'UNCLAIMED' ? '#297b99' : 'white',
          'color': activeBtn == 'UNCLAIMED' ? 'white' : 'black',
        }"
        @click="buttonFive()"
      >
        Unclaimed
      </button>
    </div>
    <div class="search">
      <label>Search: </label><input id="searchInput" type="text" />
    </div>
  </div>
</template>

<script>
export default {
  name: "LeadsTypeAndSearch",
  data() {
    return {
      activeBtn: "NONE",
    };
  },

  methods: {
    buttonOne() {
      this.activeBtn = "TARGET LEADS";
    },
    buttonTwo() {
      this.activeBtn = "ALL LEADS";
    },
    buttonThree() {
      this.activeBtn = "MY LEADS";
    },
    buttonFour() {
      this.activeBtn = "SORT BY SHIPPING DATE";
    },
    buttonFive() {
      this.activeBtn = "UNCLAIMED"
    },
  },
};
</script>

<style>
.btn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: white;
  /* background-color: white; */
  border: none;
  color: black;
  padding: 12px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  margin: 0px 5px;
  border-radius: 20px;
}

.hover:hover {
  background-color: green;
}

.btn:hover {
  /* background-color: rgb(212, 212, 212); */
}

.typesAndSearch {
  text-align: center;
  display: block;
  margin: 4% 0% 10% 0%;
  position: relative;
}

.types {
  float: left;
}

.search {
  float: right;
}

#searchInput {
  width: 60%;
  height: 20px;
}
</style>