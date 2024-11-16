class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        out = []
        l = 0

        for r in range(1, len(nums)):
            if nums[r] - nums[r - 1] != 1:
                while l < r and l < len(nums) - k + 1:
                    out.append(-1)
                    l += 1
                l = r
            elif r - l == k - 1:
                out.append(nums[r])
                l += 1

        return out
