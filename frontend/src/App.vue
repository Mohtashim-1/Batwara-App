<template>
  <div class="mx-4 my-2">
    <router-view />
  </div>
</template>

<script setup>
import { getFriendsListResource } from '@/data/friends';

const friendList = getFriendsListResource(); // Correct variable name


import { computed, provide } from 'vue';

const friends = computed(() => {
  return friendList.list?.data || []; // Use correct variable name
});

provide("friends", friends);
</script>
