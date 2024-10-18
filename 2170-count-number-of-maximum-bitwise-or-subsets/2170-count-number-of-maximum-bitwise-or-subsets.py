class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for i in nums:
            max_or |= i

        def dfs(i, cur):
            if i == len(nums):
                return 1 if cur == max_or else 0

            return dfs(i + 1, cur) + dfs(i + 1, cur | nums[i])

        return dfs(0, 0)
