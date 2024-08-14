class Solution:
    # Helper function to count pairs with distance less than or equal to 'target_distance'
    def count_pairs_with_distance(self, nums: List[int], target_distance: int) -> int:
        # Initialize the count of pairs with distance less than or equal to 'target_distance'
        pair_count = 0

        # Initialize the left pointer for the two-pointer technique
        left_pointer = 0

        # Iterate over the sorted list with the right pointer
        for right_pointer in range(1, len(nums)):
            # Move the left pointer to maintain the distance constraint (abs(nums[right_pointer] - nums[left_pointer]) <= target_distance)
            while abs(nums[right_pointer] - nums[left_pointer]) > target_distance:
                left_pointer += 1

            # Count the number of pairs with distance less than or equal to 'target_distance'
            pair_count += right_pointer - left_pointer

        # Return the count of pairs with distance less than or equal to 'target_distance'
        return pair_count

    # Function to find the smallest distance pair in the given list of numbers
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the input list in ascending order
        nums.sort()

        # Step 2: Initialize the search range for the smallest distance pair
        min_distance = 0
        max_distance = nums[-1] - nums[0]

        # Step 3: Perform binary search to find the smallest distance pair
        while min_distance < max_distance:
            # Calculate the mid value for the current search range
            mid_distance = (min_distance + max_distance) // 2

            # Check if there are at least 'k' pairs with distance less than or equal to 'mid_distance'
            if self.count_pairs_with_distance(nums, mid_distance) >= k:
                # If yes, update the search range to the left half (smaller distances)
                max_distance = mid_distance
            else:
                # If no, update the search range to the right half (larger distances)
                min_distance = mid_distance + 1

        # Step 4: Return the smallest distance pair
        return min_distance
