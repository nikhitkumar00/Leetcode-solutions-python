class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        dp = points[0]

        for i in range(1, ROWS):
            left, right = [0] * COLS, [0] * COLS
            left[0] = dp[0]
            right[-1] = dp[-1]

            for l in range(1, COLS):
                left[l] = max(dp[l], left[l - 1] - 1)

            for r in range(COLS - 2, -1, -1):
                right[r] = max(dp[r], right[r + 1] - 1)

            dp = [max(left[j], right[j]) + points[i][j] for j in range(COLS)]

        return max(dp)