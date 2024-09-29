class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # since greatest power in 32bit of 3 is 1162261467
        return n > 0 and 1162261467 % n == 0
