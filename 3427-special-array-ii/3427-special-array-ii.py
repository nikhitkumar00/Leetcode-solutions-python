class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        group = 0

        for i in range(1, len(nums)):
            copy = nums[i-1]
            nums[i-1] = group
            if nums[i] % 2 == copy % 2:
                group += 1
        nums[-1] = group

        for i in range(len(queries)):
            queries[i] = nums[queries[i][0]] == nums[queries[i][1]]

        return queries
