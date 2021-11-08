<template>
  <div class="leads">
    <Pagination />
    <LeadsTypeAndSearch />
    <DateAndPriority />
    <div v-for="lead in leads" :key="lead.id">
      <div class="lead">
        <div :class="lead.agent ? 'claimedLead' : 'unclaimedLead'">
          <div class="row">
            <div v-if="lead.agent" class="agent">
              Agent: <b>{{ lead.agent.firstName }} {{ lead.agent.lastName }}</b>
            </div>
            <div v-else>
              <b>Unclaimed</b>
            </div>
            <div class="timeChanged">Changed: {{ lead.last_changed }}</div>
          </div>
          <div class="row">
            <div>Move date: {{ lead.estimated_ship_date }}</div>
            <div class="notesChat">
              <button class="notes" @click="notes(lead)">Notes</button>
              <div v-if="lead.notes_active" class="notesDiv">
                <div class="noteTitle">
                  <div>Notes for Lead #{{ lead.id }}</div>
                </div>
                <div
                  v-for="note in lead.note_set"
                  :key="note.id"
                  class="notesFor"
                >
                  <div class="noteTime">{{ note.time }}</div>
                  <div class="noteSender">
                    <b
                      >{{ note.sender.firstName }}
                      {{ note.sender.lastName }}:</b
                    >
                    {{ note.message }}
                  </div>
                </div>
                <!-- <div class="noteSubmit">
                  <div class="noteSubmit2">
                    <input
                      class="notesInput"
                      type="text"
                      v-model="noteText"
                    /><button @click="addNote(lead.id)" class="notesSubmitBtn">
                      Submit
                    </button>
                  </div>
                </div> -->
              </div>
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
                class="priorityLead priorityOneLead"
                @click="priorityFilter = 'No priority'"
              ></button>
              <span class="tooltiptextLead">No priority</span>
            </div>
            <div class="tooltipLead">
              <button
                class="priorityLead priorityTwoLead"
                @click="priorityFilter = 'Bad lead'"
              ></button>
              <span class="tooltiptextLead">Bad lead</span>
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
                @click="priorityFilter = 'Booked lead'"
              ></button>
              <span class="tooltiptextLead">Potential lead</span>
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
        <div class="lower">
          <div class="leadId">
            <div>{{ lead.id }}</div>
          </div>
          <div>
            <button
              :class="lead.active ? 'plus-button rotate' : 'plus-button'"
              @click="lead.active = !lead.active"
            ></button>
          </div>
          <div class="name">{{ lead.first_name }} {{ lead.last_name }}</div>
          <div>
            <button class="phoneNumber">{{ lead.phone }}</button>
          </div>
          <div>
            <!-- <button>{{lead.phone_number}}</button> -->
            {{ lead.phone_number }}
          </div>
          <div class="entireLocation">
            <div class="location">
              <div class="oneLocation">{{ lead.pickup_city }},</div>
              <div class="oneLocation">{{ lead.pickup_state_code }}</div>
              <div class="oneLocation">({{ lead.pickup_zip }})</div>
            </div>
            <div class="arrow"></div>
            <div class="location">
              <div class="oneLocation">{{ lead.dropoff_city }},</div>
              <div class="oneLocation">{{ lead.dropoff_state_code }},</div>
              <div class="oneLocation">({{ lead.dropoff_zip }})</div>
            </div>
          </div>
          <div class="arrows">
            <div class="oneArrow"></div>
            <div class="threeArrows">
              <div class="oneArrow differArrows"></div>
              <div class="oneArrow differArrows"></div>
              <div class="oneArrow differArrows"></div>
            </div>
          </div>
          <div>Created {{ lead.time_created }}</div>
          <div v-if="!lead.agent">
            <button class="claim" @click="claimLead(lead)">Claim</button>
          </div>
          <div v-else>
            <!-- <button class="claimed" @click="unclaimLead(lead)">Unclaim</button> -->
            <button class="claimed" @click="claimLead(lead)">Reclaim</button>
          </div>
        </div>
        <div v-if="lead.active" class="fallingInfo">
          <div class="fallingColumn">
            <div><b>Name:</b></div>
            <div>{{ lead.first_name }} {{ lead.last_name }}</div>
            <div><b>Email:</b></div>
            <div>{{ lead.email }}</div>
            <div><b>Phone:</b></div>
            <div>{{ lead.phone }}</div>
            <div><b>Time created:</b></div>
            <div>{{ lead.time_created }}</div>
          </div>
          <div class="fallingColumn">
            <div><b>Vehicle:</b></div>
            <div>
              {{ lead.make1 }} {{ lead.model1 }} {{ lead.year1 }} ({{
                lead.vehicle_type_id1
              }})
            </div>
            <div><b>Misc:</b></div>
            <div>Car condition: {{ lead.vehicle_runs }}</div>
            <div>Carrier type: {{ lead.ship_via_id }}</div>
          </div>
          <div class="fallingColumn">
            <div><b>From:</b></div>
            <div>
              {{ lead.pickup_city }}, {{ lead.pickup_state_code }} ({{
                lead.pickup_zip
              }})
            </div>
            <div><b>To:</b></div>
            <div>
              {{ lead.dropoff_city }}, {{ lead.dropoff_state_code }} ({{
                lead.dropoff_zip
              }}
            </div>
            <div><b>Move date:</b></div>
            <div>{{ lead.estimated_ship_date }}</div>
          </div>
        </div>
      </div>
    </div>
    <!-- <button @click="test()">Test</button> -->
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
      //:class="lead.agent ? 'claimedLead' : 'lead'

      leads: [
        // {
        //   id: 1,
        //   first_name: "Damjan",
        //   last_name: "Banjac",
        //   email: "baki@gmail.com",
        //   phone_number: "064124124",
        //   time_created: "29-10-2021",
        //   last_changed: "29-10-2021",
        //   year1: "2019",
        //   make1: "Toyota",
        //   model1: "Yarris",
        //   vehicle_type_id1: "Hatchback",
        //   pickup_city: "Sabatka",
        //   pickup_state_code: "SU",
        //   pickup_zip: 20000,
        //   dropoff_city: "Novi Sad",
        //   dropoff_state_code: "NS",
        //   dropoff_zip: 21000,
        //   estimated_ship_date: "31-10-2021",
        //   vehicle_runs: "Yes",
        //   ship_via_id: "Open",
        //   priority: "No priority",
        //   agent: "Maria",
        // },
        // {
        //   id: 2,
        //   first_name: "Damjan",
        //   last_name: "Pantic",
        //   email: "panta@gmail.com",
        //   phone_number: "512521512",
        //   time_created: "08-10-2021",
        //   last_changed: "10-10-2021",
        //   year1: "2020",
        //   make1: "Audi",
        //   model1: "A4",
        //   vehicle_type_id1: "Coupe",
        //   pickup_city: "Negotin",
        //   pickup_state_code: "NE",
        //   pickup_zip: 10000,
        //   dropoff_city: "Novi Sad",
        //   dropoff_state_code: "NS",
        //   dropoff_zip: 21000,
        //   estimated_ship_date: "14-10-2021",
        //   vehicle_runs: "Yes",
        //   ship_via_id: "Closed",
        //   priority: "No priority",
        //   agent: undefined,
        // },
      ],
      //   notes: [{
      //       id: 1,
      //       time: "11/11/2011",
      //       message: "Mesageee",
      //       sender: "Sendeeer"
      //   }],
      auth: false,
      noteText: "",
    };
  },

  computed: {
    getId() {
      return this.$store.state.id;
    },
  },

  async mounted() {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/user", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      // response.json().then(result => console.log(result))

      const content = await response.json();
      console.log(content);
      console.log("ID ", content.id);
      if (response.status == 200) {
        this.$store.dispatch("setId", content.id);
        if (content.is_superuser) {
          this.$store.dispatch("setAdmin", true);
        } else {
          this.$store.dispatch("setAdmin", false);
        }
      } else {
        this.$store.dispatch("setAdmin", false);
      }
    } catch (e) {
      await this.$store.dispatch("setAdmin", false);
    }

    const response = await fetch("http://127.0.0.1:8000/api/leads", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    });

    const leads = await response.json();
    this.leads = leads;
  },

  methods: {
    async test() {
      const response = await fetch("http://127.0.0.1:8000/api/test", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      console.log(response);
      console.log(response.data);
      const content = await response.json();
      console.log(content);
      console.log("IDE CONTENT", content);
    },

    async claimLead(lead) {
      const idLead = lead.id;
      const idUser = this.$store.state.id;
      const response = await fetch("http://127.0.0.1:8000/api/lead/claim", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          idLead,
          idUser,
        }),
      });
      const content = await response.json();
      if (response.status == 200) {
        console.log("CONTENT ", content);
        console.log("PRE ", this.leads);
        this.leads = content;
        console.log("POSLE ", this.leads);
      }
    },

    // async unclaimLead(lead) {
    //   console.log("UNCLAIM");
    //   const idLead = lead.id;
    //   const response = await fetch("http://127.0.0.1:8000/api/lead/unclaim", {
    //     method: "PUT",
    //     headers: { "Content-Type": "application/json" },
    //     credentials: "include",
    //     body: JSON.stringify({
    //       idLead,
    //     }),
    //   });
    //   const content = await response.json();
    //   console.log(content);
    //   this.leads = content;
    // },

    notes(lead) {
      console.log("notes");
      let leadIsActive = false;
      if (lead.notes_active === false) {
        leadIsActive = true;
      }
      for (let iterator in this.leads) {
        this.leads[iterator].notes_active = false;
      }
      if (leadIsActive === true) {
        lead.notes_active = true;
      }
      this.noteText = "";
    },
    async addNote(lead) {
      let sender = this.$store.state.id;
      let message = this.noteText;
      const response = await fetch("http://127.0.0.1:8000/api/note/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          sender,
          message,
          lead,
        }),
      });

      const content = await response.json();
      console.log("CONTENT ", content);

      for (let iterator in this.leads) {
        if (this.leads[iterator].id == lead) {
          console.log("LEAD ", this.leads[iterator]);
          console.log("NOTES ", this.leads[iterator].note_set);
          let adObject = {
            sender: "neki",
            message: "por",
            time: "time",
            lead: lead,
          };
          this.leads[iterator].note_set.push(adObject);
        }
      }

      //   console.log("LEAD ID ", lead);
      //   console.log("LEAD ", this.leads[parseInt(lead)])
      //   console.log("NOTE SET ", this.leads[parseInt(lead)].note_set)
      //   console.log("NOTES ", this.leads[lead].note_set);
    },
  },
};
</script>

<style>
.lead {
  background-color: white;
  /* background-color: rgb(219,219,219); */
  margin: 15px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.unclaimedLead {
  background-color: white;
}

.claimedLead {
  background-color: rgb(219, 219, 219);
  /* margin: 15px; */
  /* box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); */
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
  margin: 30px;
}

.notes {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #297b99;
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  border-radius: 20px;
  width: 80px;
}

.priorityLead {
  height: 15px;
  width: 15px;
  border: 0.7px solid white;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  margin: 5px;
}

.priorityButtonsLead {
  display: flex;
  margin: 5px;
  margin-bottom: 10px;
}

.priorityOneLead {
  background-color: rgb(219, 219, 219);
}

.priorityTwoLead {
  background-color: rgb(240, 172, 183);
}

.priorityThreeLead {
  background-color: rgb(250, 229, 111);
}

.priorityFourLead {
  background-color: rgb(142, 233, 142);
}

.priorityFiveLead {
  background-color: rgb(255, 202, 104);
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

.leadId {
  background-color: #297b99;
  color: white;
  min-width: 60px;
  font-size: 14px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  /* margin-left: -0.3%; */
}

.lower {
  display: flex;
  flex-direction: row;
  align-items: center;
  /* margin: 6px 0px; */
  border-top: 1px solid rgb(209, 209, 209);
  height: 50px;
  justify-content: space-between;
}

.plus-button {
  border: 2px solid white;
  background-color: black;
  font-size: 12px;
  height: 2.5em;
  width: 2.5em;
  border-radius: 999px;
  position: relative;
  margin: 5px;
}

.plus-button:before,
.plus-button:after {
  content: "";
  display: block;
  background-color: white;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 4px;
}

.plus-button:before {
  height: 1em;
  width: 0.25em;
}

.plus-button:after {
  height: 0.25em;
  width: 1em;
}

.rotate {
  transform: rotate(45deg);
}

.phoneNumber {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #297b99;
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  margin: 3px;
  border-radius: 20px;
}

.entireLocation {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 5px;
  /* justify-items: center; */
}

.location {
  display: flex;
  flex-direction: row;
}

.arrow {
  background: rgb(0, 0, 0);
  height: 2px;
  width: 18px;
  /* margin: 0 auto; */
  position: relative;
  cursor: pointer;
  margin: 0 5px;
}

.arrow:before,
.arrow:after {
  content: "";
  background: rgb(0, 0, 0);
  position: absolute;
  height: 2px;
  width: 5px;
}

.arrow:before {
  right: -1.8px;
  bottom: -1.5px;
  transform: rotate(-45deg);
}

.arrow:after {
  right: -1.8px;
  top: -1.2px;
  transform: rotate(45deg);
}

.arrows {
  display: flex;
  flex-direction: row;
  margin: 0 10px;
  /* align-items: space-between; */
  /* justify-content: space-between; */
}

.threeArrows {
  display: flex;
  flex-direction: row;
  margin: 0px 10px;
}

.oneArrow {
  background: rgb(0, 0, 0);
  height: 8px;
  width: 0px;
  /* margin: 0 auto; */
  position: relative;
  cursor: pointer;
  margin: auto;
}

.oneArrow:before,
.oneArrow:after {
  content: "";
  background: rgb(0, 0, 0);
  position: absolute;
  height: 2px;
  width: 12px;
}

.oneArrow:before {
  right: -1.8px;
  bottom: -1.5px;
  transform: rotate(-45deg);
}

.oneArrow:after {
  right: -1.8px;
  top: -1.2px;
  transform: rotate(45deg);
}

.differArrows {
  margin: 3px;
}

.claim {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #297b99;
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  margin: 7px;
  border-radius: 20px;
}

.name {
  margin: 5px;
}

.fallingInfo {
  background-color: white;
  /* margin: 10px; */
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.fallingColumn {
  display: flex;
  flex-direction: column;
}

.claimed {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: rgb(219, 219, 219);
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  margin: 7px;
  border-radius: 20px;
}

.notesDiv {
  max-height: 300px;
  width: 400px;
  background-color: white;
  display: flex;
  flex-direction: column;
}

.notesChat {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.noteTitle {
  color: white;
  background-color: #297b99;
  height: 40px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);

  /* align-items: center; */
  /* justify-content: center; */
  align-items: flex-start;
  justify-content: flex-start;
}

.notesFor {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.noteTime {
  color: #297b99;
  border-bottom: 2px solid #297b99;
  width: 35%;
  padding-bottom: 10px;
  margin: 3px;
  margin-left: 10px;
}

.noteSender {
  margin: 3px;
  margin-left: 10px;
}

.noteSubmit {
  display: flex;
  flex-direction: column;
  margin: 5px;
  margin-top: 5px;
  align-items: stretch;
  justify-content: stretch;
}

.notesSubmitBtn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #297b99;
  /* border-radius: 12px; */
  border: 0;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  /* height: 50px; */
  margin-top: 5px;
  text-align: center;
  width: 25%;
  border-radius: 20px;
}

.notesInput {
  /* position: relative; */
  /* width: 100%; */
  width: 75%;
}

/* .noteSubmit2 {
    display:flex;
    flex-direction: row;
    align-items: stretch;
    justify-content: stretch;
} */

.noteSubmit2 {
  display: flex;
  flex-direction: row;
}
</style>