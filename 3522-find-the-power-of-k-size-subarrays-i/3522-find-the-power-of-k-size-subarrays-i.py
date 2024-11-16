class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        out = []
        l = 0
        n = len(nums)

        for r in range(1, n):
            if nums[r] - nums[r - 1] != 1:
                out.extend([-1] * max(0, min(r - l, n - k + 1 - l)))
                l = r
            elif r - l == k - 1:
                out.append(nums[r])
                l += 1
        out.extend([-1] * max(0, n - k + 1 - l))

        return out
