<template>
  <v-list two-line>
    <template v-for="tweet in tweets">
      <v-list-tile :key="tweet.content" avatar>
        <v-list-tile-avatar>
          <img :src="tweet.author_avatar" />
        </v-list-tile-avatar>

        <v-list-tile-content>
          <v-list-tile-title>
            <router-link :to="{ name: 'user-username', params: { username: tweet.author_username }}">
              {{ tweet.author_name }}
            </router-link>/
            @ {{ tweet.author_username }} /
            {{ tweet.created_at | timeago }}
          </v-list-tile-title>
          <v-list-tile-sub-title>
            {{ tweet.content }}
          </v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
    </template>
  </v-list>
</template>

<script>
export default {
  props: ['tweets']
};
</script>

<style></style>
