<template>
    <div>
    <div>Logged user: {{this.ide}} </div>
      <div v-for="lead in leads" :key="lead.id">
          <div class='lead'>
              {{lead.name}}
          </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Leads',
    data() {
        return {
            ide: "gas",

            leads: [
                {
                    id: 1,
                    name: "Banjac"
                },
                {
                    id: 2,
                    name: "Pantic"
                }
            ]
        }
    },

    mounted() {
        axios({
            method: 'GET',
            url: 'api/user'
        }).then(response => {
            console.log(response.data)
        })
    }
}
</script>

<style>

.lead {
    background-color: white;
    margin: 10px;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

}

</style>