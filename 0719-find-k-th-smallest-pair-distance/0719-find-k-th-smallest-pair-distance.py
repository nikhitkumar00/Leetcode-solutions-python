class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        # Helper function to count pairs with distance less than or equal to 'target_distance'
        def count_pairs_with_distance(target_distance):

            pair_count = 0
            left_pointer = 0

            for right_pointer in range(1, len(nums)):
                # Move the left pointer to maintain the distance constraint
                # (abs(nums[right_pointer] - nums[left_pointer]) <= target_distance)
                while abs(nums[right_pointer] - nums[left_pointer]) > target_distance:
                    left_pointer += 1

                # Count the number of pairs with distance less than or equal to 'target_distance'
                pair_count += right_pointer - left_pointer

            return pair_count

        #################################################################################

        # Step 1: Sort the input list in ascending order
        # This allows us to apply the two-pointer technique later
        nums.sort()

        # Step 2: Initialize the search range for the smallest distance pair
        # 'min_distance' represents the minimum possible distance (0)
        # 'max_distance' represents the maximum possible distance (difference between the largest and smallest numbers)
        min_distance = 0
        max_distance = nums[-1] - nums[0]

        # Step 3: Perform binary search to find the smallest distance pair
        while min_distance < max_distance:

            mid_distance = (min_distance + max_distance) // 2

            # Check if there are at least 'k' pairs with distance less than or equal to 'mid_distance'
            # This is done using the 'count_pairs_with_distance' helper function
            if count_pairs_with_distance(mid_distance) >= k:
                # If yes, update the search range to the left half (smaller distances)
                max_distance = mid_distance
            else:
                # If no, update the search range to the right half (larger distances)
                min_distance = mid_distance + 1

        return min_distance
