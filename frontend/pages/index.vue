<template>
  <div>
    <home :tweets="tweets" />
  </div>
</template>

<script>
import home from "~/components/home";
import AppApi from "~apijs";

export default {
  components: {
    home
  },
  data() {
    return {};
  },
  computed: {
    logged_user () {
      return this.$store.getters.logged_user
    },
  },
  asyncData() {
    return AppApi.list_tweets().then(result => {
      return { tweets: result.data };
    });
  }
};
</script>

<style></style>
