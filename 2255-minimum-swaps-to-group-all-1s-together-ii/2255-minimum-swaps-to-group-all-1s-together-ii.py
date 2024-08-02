class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        total_ones = nums.count(1)
        length = len(nums)
        if total_ones == 0 or total_ones == length:
            return 0

        nums = nums[:] + nums[:]

        current_ones = nums[: total_ones].count(1)
        out = total_ones - current_ones

        for i in range(1, length):
            current_ones = current_ones - nums[i-1] + nums[i+total_ones-1]
            out = min(out, total_ones - current_ones)
        
        return out