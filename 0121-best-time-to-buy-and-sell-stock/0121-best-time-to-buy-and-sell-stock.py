class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        buy = prices[0]

        for sell in prices:
            out = max(out, sell - buy)
            buy = min(buy, sell)

        return out
