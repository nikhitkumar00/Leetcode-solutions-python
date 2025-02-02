class Solution:
    def check(self, nums: List[int]) -> bool:
        out = sorted(nums)

        for i in range(len(nums)):
            if out == nums[i:] + nums[:i]:
                return True
        return False
