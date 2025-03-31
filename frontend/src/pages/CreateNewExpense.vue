<template>
  <PageHeader heading="New Expense">
      <template #actions>
          <Button> Save </Button>
      </template>
  </PageHeader>

  <div class="space-y-3">
      <FormControl label="Description" type="text" placeholder="Pizza from Zomato" />
      <FormControl label="Amount" type="number" placeholder="0.00" />
      <FormControl label="Expense Date" type="date" />
  </div>

  <div class="pt-3 text-gray-800 font-semibold text-lg">
      Paid by <Button variant="outline">You</Button> and split
      <Dropdown :options="[
          {
              label: 'Equally',
              onClick: () => { splitMethod = 'Equally' },
          },
          {
              label: 'Manually',
              onClick: () => { splitMethod = 'Manually' },
          },
      ]" :button="{ label: splitMethod, variant: 'outline' }" />
  </div>

  <div class="mb-2">
    <h3>Split With:</h3>
    <Autocomplete 
      placeholder="Select Friends" 
      :options="friendAutocompleteOptions" 
      v-model="seletedFriends" 
      :multiple="true" 
    />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import PageHeader from '../components/common/Heading.vue';
import { FormControl, Dropdown, Autocomplete } from 'frappe-ui';
import { createResource } from 'frappe-ui';

// Fetch friends from API
const friendsResource = createResource({
url: 'batwara.api.get_friends_for_current_user',
method: 'GET',
auto: true,
});

const friends = ref([]);

// Update `friends` when API response changes
watch(() => friendsResource.data, (newData) => {
if (newData) {
  friends.value = newData;
}
}, { immediate: true });

const splitMethod = ref("Equally");
const seletedFriends = ref([]);

const friendAutocompleteOptions = computed(() => {
return friends.value.map(f => ({
  label: f.full_name,
  value: f.friend
}));
});

// Debugging
watch(seletedFriends, () => {
console.log("Selected friends:", seletedFriends.value);
});
</script>
