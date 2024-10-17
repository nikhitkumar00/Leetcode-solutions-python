class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        out = 0

        for i in nums:
            v = str(i)
            out += int(max(v) * len(v))

        return out
