<template>
  <div>
    <usercard :user="user" />
    <timeline :tweets="tweets" />
  </div>
</template>

<script>
import timeline from "~/components/timeline.vue";
import usercard from "~/components/usercard.vue";

export default {
  components: {
    timeline,
    usercard
  },
  props: ["user", "tweets"]
};
</script>

<style></style>
