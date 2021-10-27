<template>
    <div>
        <h1>Test 123</h1>
    </div>
</template>

<script>

import axios from 'axios';
export default {
    name: 'UnreadMails',


    mounted() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/all/messages',
      }).then(response => {
        console.log(response.data)
      }).catch(error => {
        console.log(error);
      });
    },
}


</script>

<style>


</style>