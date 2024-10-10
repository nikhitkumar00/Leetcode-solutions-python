class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums) - 1
        cur = nums[i]

        for val in reversed(nums):
            if val > cur:
                cur = val
            max_right[i] = cur
            i -= 1

        l, r = 0, 1
        out = 0
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            out = max(out, r - l)
        return out
