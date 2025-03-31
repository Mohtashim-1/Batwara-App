<template>
  <PageHeader heading="New Expense">
    <template #actions>
      <Button :loading="expenseListResource.insert.Loading" @click="saveExpense"> Save </Button>
    </template>
  </PageHeader>

  <div class="space-y-3">
    <div>
      <ErrorMessage :message="expenseListResource.insert.error" />
    </div>
    <FormControl v-model="expenseDetails.description" label="Description" type="text" placeholder="Pizza from Zomato" />
    <FormControl v-model.number="expenseDetails.amount" label="Amount" type="number" placeholder="0.00" />
    <FormControl v-model="expenseDetails.date" label="Expense Date" type="date" />
  </div>

  <div class="pt-3 text-gray-800 font-semibold text-lg">
    Paid by <Button variant="outline">You</Button> and split
    <Dropdown :options="[
      {
        label: 'Equally',
        onClick: () => { expenseDetails.split_method = 'Equally' },
      },
      {
        label: 'Manually',
        onClick: () => { expenseDetails.split_method = 'Manually' },
      },
    ]" :button="{ label: splitMethod, variant: 'outline' }" />
  </div>

  <div class="mb-2">
    <h3>Split With:</h3>
    <Autocomplete placeholder="Select Friends" :options="friendAutocompleteOptions"
      v-model="expenseDetails.selected_friends" :multiple="true" />
  </div>
</template>

<script setup>
import { ref, computed, watch, reactive } from 'vue';
import PageHeader from '../components/common/Heading.vue';
import { FormControl, Dropdown, Autocomplete, createListResource, ErrorMessage } from 'frappe-ui';
import { createResource } from 'frappe-ui';
import { sessionUser } from "@/data/session";
import dayjs from "dayjs";
import { useRouter } from 'vue-router';

const router = useRouter();
 

window.dayjs = dayjs

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


const today = dayjs().format("YYYY-MM-DD")
const expenseDetails = reactive({
  description: '',
  amount: 0.0,
  currency: 'PKR',
  date: today,
  split_method: "Equally",
  selected_friends: [{
    label: 'You',
    value: sessionUser(),
  }]
})
const splitMethod = ref("Equally");
const seletedFriends = ref([{
  label: 'You',
  value: sessionUser(),

}]);

const friendAutocompleteOptions = computed(() => {
  const options = friends.value.map(f => ({
    label: f.full_name,
    value: f.friend
  }));
  options.push({
    label: "You",
    value: sessionUser(),
  })
  return options;
});

// Debugging
watch(expenseDetails, () => {
  console.log("Selected friends:", expenseDetails);
});

const expenseListResource = createListResource({
  doctype: "Expense",

}
)
function saveExpense() {
  expenseListResource.insert.submit(
    {
      ...expenseDetails,
      paid_by: sessionUser(),
      expense_split: expenseDetails.selected_friends.map((f) => ({
      user: f.value,

    }))
    },
    {
      onSuccess(){
        router.replace({name:"Dashboard"})
      }
    }
  )
}
</script>
