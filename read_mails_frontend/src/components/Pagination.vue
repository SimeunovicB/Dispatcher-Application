<template>
  <div class="pagination">
    <button id="previous" class="paginationBtn">Previous page</button>
    <span><label>Page </label>
    <input id="pageInput" type="number" /></span>
    <button id="next" class="paginationBtn">Next page</button>
  </div>
</template>

<script>
export default {
  name: "Pagination",
};
</script>

<style>

.paginationBtn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #11bfeb;
  border: none;
  color: white;
  padding: 12px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
  text-transform: uppercase;
}

/* .pagination {
  text-align: center;
  display: block;
  margin: 2% 0%;
  position: relative;
}

#previous {
    float: left;
}

#next {
    float: right;
} */

.pagination {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
    margin: 2% 0%;

}

#pageInput {
    width: 20%;
}





</style>