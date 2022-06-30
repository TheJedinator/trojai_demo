<template>
  <div class="home">
    {{ data }}
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import get_data from "@/services/api-service"
import HelloWorld from "@/components/HelloWorld.vue" // @ is an alias to /src

@Component({
  components: {
    HelloWorld,
  },
})
export default class HomeView extends Vue {
  data = "test"
  mounted() {
    get_data("http://localhost:8000/").then((x) => {
      this.data = x.message
    })
  }
}
</script>
