class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        prev = float("inf")
        flag = 1

        while i < len(nums):
            deleted = 0

            if nums[i] == prev:
                if flag == 0:
                    nums.pop(i)
                    deleted = 1
                else:
                    flag -= 1
            else:
                flag = 1
                prev = nums[i]

            if deleted == 0:
                i += 1

        return len(nums)
