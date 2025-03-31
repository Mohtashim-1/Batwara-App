<template>
  

  <PageHeader heading="Your friends " />
  <div v-if="friends.length">
    <ol>
      <!-- Display only the full_name (username) -->
      <li v-for="friend in friends" :key="friend.email">

        <div class="flex items-center space-x-3 p-1">
          <Avatar :label="getInitials(friend.full_name)" size="xl" :url="friend.user_image" />
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

  <div class="mt-5">

      <Button :link="'/new-expense'" variant="solid" theme="blue">Add Expense</Button>
  </div>
</template>

<script setup>
// import { inject } from 'frappe-ui';
import { inject } from 'vue';
import { computed } from 'vue';
import { Avatar } from 'frappe-ui';
import  PageHeader from '../components/common/Heading.vue'

const friends = inject("friends")
</script>
