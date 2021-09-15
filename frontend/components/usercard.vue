<template>
  <v-card color="cyan darken-2" class="white--text">
    <v-layout>
      <v-flex xs7>
        <v-card-title primary-title>
          <div>
            <div class="headline">{{ user.username }}</div>
            <div>@{{ user.username }}</div>
          </div>
        </v-card-title>
      </v-flex>
      <v-avatar size="200px">
        <img
          src="https://cdn.vuetifyjs.com/images/cards/foster.jpg"
          alt="Avatar"
        >
      </v-avatar>
    </v-layout>
    <v-divider light></v-divider>
  </v-card>
</template>

<script>
export default {
  props: ['user']

}
</script>

<style>

</style>