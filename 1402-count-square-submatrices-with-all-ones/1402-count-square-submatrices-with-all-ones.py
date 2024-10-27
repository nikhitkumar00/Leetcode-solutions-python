class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        count = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    
                    count += dp[r][c]

        return count
