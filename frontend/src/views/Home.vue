<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/UCR_Icon_BluBG.png" width="30%"/>
    <ol>
    <li v-for="value in values" :key="value.name">
      <b>{{value.name}}</b>
    </li>
    </ol>
    <HelloWorld msg="Welcome to Your Vue.js App (UCR)" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
//import Vue from "vue";

export default {
  name: "HomePage",
  components: {
    HelloWorld,
  },
  data () {
    return {
      values: []
    }
  },
  created: function () {
    this.$http.get('/api/foos/').then((response) => {
      console.log(response.data)
      this.values = response.data
    })
    console.log("Created")
  }
};
</script>
