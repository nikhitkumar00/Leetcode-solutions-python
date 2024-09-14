class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = max(nums)
        cur = 0
        out = 0

        for i in nums:
            if i == maxx:
                cur += 1
            else:
                cur = 0
            out = max(out, cur)

        return out
