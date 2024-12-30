class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = [0] * (high+1)
        dp[0] = 1

        for i in range(min(zero,one),high+1):
            dp[i] = (dp[i-zero]+dp[i-one]) % (10**9+7)
        
        return sum(dp[low:]) % (10**9+7)