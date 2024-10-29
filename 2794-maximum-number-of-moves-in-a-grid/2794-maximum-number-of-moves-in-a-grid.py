class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        directions = (-1, 0, 1)

        def dfs(row, col):
            if col == COLS - 1:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            maxx = 0
            for d in directions:
                nr, nc = row + d, col + 1

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] > grid[row][col]:
                    maxx = max(maxx, 1 + dfs(nr, nc))

            dp[row][col] = maxx
            return maxx

        out = 0
        for i in range(ROWS):
            out = max(out, dfs(i, 0))
        return out
