class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        lds = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        out = float("inf")
        for i in range(len(nums)):
            if lis[i] > 1 and lds[i] > 1:
                out = min(out, len(nums) + 1 - lis[i] - lds[i])

        return out
