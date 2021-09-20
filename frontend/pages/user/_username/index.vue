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
    
    return Promise.all([AppApi.get_user_details(username), AppApi.list_tweets(username)]).then(results => {

      console.log(results)
      return {
        user: results[0].data,
        tweets: results[1].data
      }
    })
  },
  data () {
    return {
      tweets: []
    }
  }
}
</script>

<style></style>
