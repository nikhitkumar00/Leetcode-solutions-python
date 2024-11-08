class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = [(1 << maximumBit) - 1]
        for i in nums:
            ans.append(ans[-1] ^ i)
        return ans[:0:-1]
