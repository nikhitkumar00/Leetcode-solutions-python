class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = nums[0]
        maxVal = cur
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                cur = nums[i]
            maxVal = max(maxVal, cur)
        return maxVal
