class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        out = l = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            out = max(out, r - l + 1)
        return out
