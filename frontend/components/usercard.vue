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
        <v-btn
          v-if="logged_user"
          @click="toggle_follow(user)"
          :color="user.is_following ? 'error' : 'success'"
          :loading="loading"
        >
          {{ user.is_following ? "Unfollow" : "Follow" }}
        </v-btn>
      </v-flex>

      <v-avatar size="200px">
        <img :src="user.author_avatar" alt="Avatar" />
      </v-avatar>
    </v-layout>
    <v-divider light></v-divider>
  </v-card>
</template>

<script>
import AppApi from "~apijs";
import Snacks from "~/helpers/snacks.js";

export default {
  props: ["user"],
  data() {
    return {
      loading: false
    };
  },
  computed: {
    logged_user() {
      return this.$store.getters.logged_user;
    }
  },
  methods: {
    toggle_follow() {
      this.loading = true;
      AppApi.toggle_follow(this.user.username, !this.user.is_following).then(
        () => {
          this.user.is_following = !this.user.is_following;
          this.loading = false;
        }
      );
      Snacks.show(this.$store, {
        color: this.user.is_following ? "error" : "success",
        text: this.user.is_following
          ? `Unfollowed ${this.user.username}`
          : `Following ${this.user.username}`
      });
    }
  }
};
</script>

<style></style>
