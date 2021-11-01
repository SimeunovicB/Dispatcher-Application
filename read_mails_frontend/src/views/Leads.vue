<template>
  <div class="leads">
    <Pagination />
    <LeadsTypeAndSearch />
    <DateAndPriority />

    <div v-for="lead in leads" :key="lead.id">
      <div class="lead">
        <div class="row">
          <div v-if="lead.agent" class="agent">
            Agent: <b>{{ lead.agent }}</b>
          </div>
          <div v-else>
            <b>Unclaimed</b>
          </div>
          <div class="timeChanged">Changed: {{ lead.last_changed }}</div>
        </div>
        <div class="row">
          <div>Move date: {{ lead.move_date }}</div>
          <div>
            <button class="notes">Notes</button>
          </div>
        </div>
        <div class="row">
          <div>Priority: {{ lead.priority }}</div>
          <div>Follow-up: Not set</div>
          <!-- <div class="priority">
                Priority: {{lead.priority}}
            </div>
            <div>
                Follow-up: Not set
            </div> -->
        </div>
        <div class="priorityButtonsLead">
          <div class="tooltipLead">
            <button
              class="priorityLead priorityTwoLead"
              @click="priorityFilter = 'No priority'"
            ></button>
            <span class="tooltiptextLead">No priority</span>
          </div>
          <div class="tooltipLead">
            <button
              class="priorityLead priorityThreeLead"
              @click="priorityFilter = 'Future lead'"
            ></button>
            <span class="tooltiptextLead">Future lead</span>
          </div>
          <div class="tooltipLead">
            <button
              class="priorityLead priorityFourLead"
              @click="priorityFilter = 'Hot lead'"
            ></button>
            <span class="tooltiptextLead">Hot lead</span>
          </div>
          <div class="tooltipLead">
            <button
              class="priorityLead priorityFiveLead"
              @click="priorityFilter = 'Bad lead'"
            ></button>
            <span class="tooltiptextLead">Bad lead</span>
          </div>
          <div class="tooltipLead">
            <button
              class="priorityLead prioritySixLead"
              @click="priorityFilter = 'Booked lead'"
            ></button>
            <span class="tooltiptextLead">Booked lead</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import {useStore} from 'vuex';
import Pagination from "../components/Pagination.vue";
import LeadsTypeAndSearch from "../components/LeadsTypeAndSearch.vue";
import DateAndPriority from "../components/DateAndPriority.vue";
export default {
  name: "Leads",
  components: { Pagination, LeadsTypeAndSearch, DateAndPriority },
  data() {
    return {
      ide: "gas",

      leads: [
        {
          id: 1,
          name: "Damjan",
          surname: "Banjac",
          email: "baki@gmail.com",
          phone_number: "064124124",
          time_created: "29-10-2021",
          last_changed: "29-10-2021",
          car_year: "2019",
          car_model: "Yarris",
          car_type: "Hatchback",
          pickup_city: "Sabatka",
          delivery_city: "Novi Sad",
          move_date: "31-10-2021",
          priority: "No priority",
          agent: "Maria",
        },
        {
          id: 2,
          name: "Damjan",
          surname: "Pantic",
          email: "panta@gmail.com",
          phone_number: "dackey@gmail.com",
          time_created: "08-10-2021",
          last_changed: "10-10-2021",
          car_year: "2020",
          car_model: "A4",
          car_type: "Coupe",
          pickup_city: "Negotin",
          delivery_city: "Novi Sad",
          move_date: "14-10-2021",
          priority: "No priority",
          agent: undefined,
        },
      ],
      auth: false,
      //   store: useStore()
    };
  },

  async mounted() {
    console.log("IDDDDDE");

    console.log("ide gas");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/user", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      // response.json().then(result => console.log(result))

      const content = await response.json();
      console.log(content);
      // await this.$store.dispatch('setAuth', true);
      if (response.status == 200) {
        this.$store.dispatch("setAuth", true);
      } else {
        this.$store.dispatch("setAuth", false);
      }
    } catch (e) {
      await this.$store.dispatch("setAuth", false);
    }
  },

  methods: {
    async ajde() {
      console.log("ide gas");
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
      }
    },
  },
};
</script>

<style>
.lead {
  background-color: white;
  margin: 10px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.agentAndTimeChanged {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 6px;
}

.moveDateAndNotes {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 6px;
}

.row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 6px;
}

.leads {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.notes {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #11bfeb;
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
}

.priorityLead {
  height: 15px;
  width: 15px;
  border: 0.7px solid white;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  margin: 5px;
}

.priorityButtonsLead{
    display: flex;
  margin-left: 10px;
}

.priorityOneLead {
  background-color: rgb(241, 241, 241);
}

.priorityTwoLead {
  background-color: rgb(219, 219, 219);
}

.priorityThreeLead {
  background-color: rgb(250, 229, 111);
}

.priorityFourLead {
  background-color: rgb(142, 233, 142);
}

.priorityFiveLead {
  background-color: rgb(240, 172, 183);
}

.prioritySixLead {
  background-color: rgb(105, 214, 233);
}

.tooltipLead {
  position: relative;
  display: inline-block;
}

.tooltipLead .tooltiptextLead {
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

.tooltipLead:hover .tooltiptextLead {
  visibility: visible;
}
</style>