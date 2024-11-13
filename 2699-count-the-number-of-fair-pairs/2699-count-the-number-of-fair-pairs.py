class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()
        out = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]

            low_idx = bisect_left(nums, low, i + 1)
            up_idx = bisect_right(nums, up, i + 1) - 1

            out += max(0, up_idx - low_idx + 1)

        return out
