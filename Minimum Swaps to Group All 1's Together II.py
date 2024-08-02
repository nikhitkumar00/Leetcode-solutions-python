class Solution:
    def minSwaps(self, nums) -> int:

        # Count the total number of ones in the array
        total_ones = nums.count(1)
        length = len(nums)

        # If there are no ones or if all are ones, no swaps are needed
        if total_ones == 0 or total_ones == length:
            return 0

        # Duplicate the array to handle circular nature
        nums = nums[:] + nums[:]

        # Count the number of ones in the first window of size 'total_ones'
        current_ones = nums[:total_ones].count(1)
        out = total_ones - current_ones

        # Slide the window across the duplicated array and count the minimum swaps needed
        for i in range(1, length):
            current_ones = current_ones - nums[i - 1] + nums[i + total_ones - 1]
            out = min(out, total_ones - current_ones)

        return out