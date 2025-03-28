<template>
  <h2 class="font-bold text-gray-900">Your friends</h2>
  <div v-if="friends.length">
    <ol>
      <!-- Display only the full_name (username) -->
      <li v-for="friend in friends" :key="friend.email">
        
        <div class="flex items-center space-x-3 p-1">
  <Avatar :label="getInitials(friend.full_name)" size="xl" :url="friend.user_image"/>
  <div>
    {{ friend.full_name }}
  </div>
</div>


      </li>
    </ol>
  </div>
  <div v-else>
    <p>No friends found.</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { createListResource, Avatar } from 'frappe-ui';
import { sessionUser } from '../data/session'

const friendResource = createListResource({
  doctype: "Friend Mapping",
  fields: ["b as friend", "b.full_name as full_name", "b.user_image as user_image"],  // Fetch 'full_name' as part of the 'b' object
  filters: {
    "a": sessionUser()  // Filter by the current user
  },
  orderBy: 'friend',  // Order by the 'friend' field (email)
  auto: true
})

const friends = computed(() => {
  if (friendResource.list.data) {
    return friendResource.list.data.map(friend => ({
      email: friend.friend,        // Store the email
      full_name: friend.full_name  // Store the full name
    }));
  }
  return [];
})

function getInitials(full_name){
  return full_name.split(" ").map(part => part[0].toUpperCase()).join("")
}
</script>
