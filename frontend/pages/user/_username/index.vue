<template>
  <h1>pagina do usuario {{ username }}</h1>
</template>

<script>
export default {
  asyncData (context) {
    console.log(context)
    return {
      username: context.params.username || ""
    }
  },
  data () {
    return {}
  }
}
</script>

<style>

</style>