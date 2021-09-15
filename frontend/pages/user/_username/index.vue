<template>
  <viewuser :user="user" :tweets="tweets" />
</template>

<script>
import viewuser from "~/components/viewuser";
import AppApi from "~apijs"

export default {
  components: {
    viewuser
  },
  async asyncData (context) {
    const username = context.params.username || ""
    const tweets = await AppApi.list_tweets(username)
    return {
      user: {
        username
      },
      tweets: tweets.data.tweets
    }
  },
  data () {
    return {
      tweets: []
    }
  }
}
</script>

<style></style>
