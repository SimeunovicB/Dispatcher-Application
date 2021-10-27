<template>
  <div class="dateAndPriorityComponent">
    <div class="btnAndPriorities">
      <button class="btn">Date range</button>
      <div class="priorityDiv">
        <label>Priority filter: {{priorityFilter}}</label>
        <div class="priorityButtons">
          <div class="tooltip">
            <button class="priority priorityOne" @click='priorityFilter = "All"'></button
            ><span class="tooltiptext">All</span>
          </div>
          <div class="tooltip">
            <button class="priority priorityTwo" @click='priorityFilter = "No priority"'></button>
            <span class="tooltiptext">No priority</span>
          </div>
          <div class="tooltip">
            <button class="priority priorityThree" @click='priorityFilter = "Future lead"'></button>
            <span class="tooltiptext">Future lead</span>
          </div>
          <div class="tooltip">
            <button class="priority priorityFour" @click='priorityFilter = "Hot lead"'></button>
            <span class="tooltiptext">Hot lead</span>
          </div>
          <div class="tooltip">
            <button class="priority priorityFive" @click='priorityFilter = "Bad lead"'></button>
            <span class="tooltiptext">Bad lead</span>
          </div>
          <div class="tooltip">
            <button class="priority prioritySix" @click='priorityFilter = "Booked lead"'></button>
            <span class="tooltiptext">Booked lead</span>
          </div>
        </div>
      </div>
    </div>
    <div class="datedate">
      <div class="dates">
        <label>Range start:</label>
        <input class="date" type="date" v-model="selected"/>
      </div>
      <div class="dates">
        <label>Range end:</label>
        <input class="date" type="date" placeholder="from" />
      </div>
    </div>
  </div>
</template>

<script>
</script>
<script>
export default {
  name: "DateAndPriority",
  components: {},
  data() {
    return {
      priorityFilter: "None",
      selected: "date",
      proba: "ide gas"
    };
  },
};
</script>

<style>
.dateAndPriorityComponent {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.btnAndPriorities {
  display: flex;
  flex-direction: row;
}

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
}

.btn:hover {
  background-color: rgb(209, 209, 209);
}

.priority {
  height: 15px;
  width: 15px;
  border: 0.7px solid white;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  margin: 5px;
}

.priorityOne {
  background-color: rgb(241, 241, 241);
}

.priorityTwo {
  background-color: rgb(219, 219, 219);
}

.priorityThree {
  background-color: rgb(250, 229, 111);
}

.priorityFour {
  background-color: rgb(142, 233, 142);
}

.priorityFive {
  background-color: rgb(240, 172, 183);
}

.prioritySix {
  background-color: rgb(105, 214, 233);
}

.priorityButtons {
  margin-left: 10px;
}

.dates {
  display: flex;
  flex-direction: column;
}

.date {
  border: 1px;
  /* border-radius: 10px; */
  margin: 6px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.datedate {
  display: flex;
  flex-direction: row;
}

.tooltip {
  position: relative;
  display: inline-block;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: white;
  color: black;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  bottom: 100%;
  left: 50%;
  margin-left: -60px;
  /* Position the tooltip */
  position: absolute;
  z-index: 1;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>