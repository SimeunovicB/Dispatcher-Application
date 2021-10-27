<template>
  <div class="c">
      <div v-for="mail in mails" :key="mail.id">
          <label>{{mail.subject}}</label>
      </div>
  </div>
</template>

<script>

import axios from "axios";
export default {
    name: 'AllMails',
    data() {
      return {
        mails: []
      }
    },


    mounted() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/all/messages',
      }).then(response => {
        console.log(response.data)
        this.mails = response.data;
      }).catch(error => {
        console.log(error);
      });
    },
}
</script>

<style>

.c {
    display: flex;
    background-color: rgb(245, 245, 245);
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    width: 20%;
  }

</style>