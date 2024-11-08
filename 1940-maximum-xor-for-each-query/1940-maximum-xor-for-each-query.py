class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for i in nums:
            xor = xor ^ i

        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        for i in range(len(nums)):
            ans[i] = xor ^ mask
            xor = xor ^ nums[len(nums) - 1 - i]

        return ans
