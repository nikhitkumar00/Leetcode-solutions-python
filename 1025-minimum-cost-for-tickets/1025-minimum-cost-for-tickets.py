class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        traveldays = set(days)
        dp = [0] * 366
        for i in range(1, 366):
            if i not in traveldays:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[i - 7] + costs[1] if i >= 7 else costs[1],
                    dp[i - 30] + costs[2] if i >= 30 else costs[2],
                )
        return dp[-1]
