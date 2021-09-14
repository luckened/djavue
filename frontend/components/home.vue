<template>
  <timeline :tweets="tweets"/>
</template>

<script>
import timeline from "~/components/timeline.vue"

export default {
  components: {
    timeline
  },
  props: ['tweets']
}
</script>

<style>

</style>