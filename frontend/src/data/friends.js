import { createResource } from 'frappe-ui'

export function getFriendsListResource() {
    const resource = createResource({
        url: 'batwara.api.get_friends_for_current_user',
        method: 'GET',  // Explicitly set the method
        cache: 'friends-list',
        auto: true,  // Ensure it fetches automatically
        onSuccess: (data) => console.log("API Response:", data),
        onError: (error) => console.error("API Error:", error)
    });

    console.log("Resource:", resource);
    return resource;
}
