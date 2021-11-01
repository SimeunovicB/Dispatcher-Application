<template>
  <div class="parent">
    <div class="users">
      <h2 class="usersHeader">Users</h2>
      <div class="usersList" v-for="user in users" :key="user.id">
        <div class="userItem">
          <div class="labele">
            <div class="label">Name:</div>
            <div class="label">{{ user.firstName }} {{ user.lastName }}</div>
          </div>
          <div class="labele">
            <div class="label">Email:</div>
            <div class="label">{{ user.email }}</div>
          </div>
          <div class="labele">
            <div v-if="user.is_active">
              <button class="deactBtn" @click="changeUserActivity(user.email)">
                Deactivate user
              </button>
            </div>
            <div v-else>
              <button class="actBtn" @click="changeUserActivity(user.email)">
                Activate user
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Users",
  data() {
    return {
      users: [],
    };
  },
  async mounted() {
    const response = await fetch("http://127.0.0.1:8000/api/users", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    });
    var content = await response.json();
    console.log(content);
    this.users = content;
  },
  methods: {
    async changeUserActivity(email) {
        console.log(email);
        // const idString = id.toString();
        // console.log(idString)
      const response = await fetch("http://127.0.0.1:8000/api/user/activity", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          email
        }),
      })
      let content = await response.json();
      console.log(content)
      for(let i in this.users) {
          if(this.users[i].email == email) {
              this.users[i].is_active = !this.users[i].is_active;
          }
      }
    },
  },
};
</script>

<style>
.parent {
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.users {
  width: 60%;
  height: 100%;
  display: flex;
  margin: 30px;
  flex-direction: column;
  align-items: center;
  color: white;
  background-color: rgb(8, 8, 41);
}

/* .usersList { */
/* border-radius: 20px; */
/* box-sizing: border-box; */
/* height: 630px; */
/* padding: 20px; */
/* width: 380px; */
/* } */

.usersList {
  width: 100%;
  display: flex;
  justify-content: center;
}

.userItem {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 16px;
  height: 80%;
  outline: 0;
  padding: 4px 20px 0;
  margin: 7px;
  width: 90%;
}

.labele {
  display: flex;
  flex-direction: row;
  margin: 10px;
  width: 33%;
  align-items: center;
  justify-content: center;
}

.label {
  margin: 3px;
}

.actBtn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #07cc69;
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  width: 100%;
}

.deactBtn {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #ff3838;
  border: none;
  color: white;
  padding: 6px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  text-transform: uppercase;
  width: 100%;
}

.input {
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 16px;
  height: 100%;
  outline: 0;
  padding: 4px 20px 0;
  width: 100%;
}
</style>