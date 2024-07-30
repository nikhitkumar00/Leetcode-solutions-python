class Solution:
    def productExceptSelf(self, nums):
        left = [0 for i in range(len(nums))]
        right = [0 for i in range(len(nums))]
        prev, past = 1, 1

        for i in range(len(nums)):
            left[i] = prev
            right[len(nums) - i - 1] = past

            prev *= nums[i]
            past *= nums[len(nums) - i - 1]

        return [a * b for a, b in zip(left, right)]
