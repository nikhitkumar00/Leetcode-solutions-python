class Solution:
    def dfs(self, r, c, grid, d):
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == 2 or grid[r][c] == 3:
                return

            grid[r][c] = 1
            if d == "U":
                r -= 1
            elif d == "D":
                r += 1
            elif d == "L":
                c -= 1
            elif d == "R":
                c += 1
        return

    def countUnguarded(self, m, n, guards, walls) -> int:
        grid = [[0] * n for _ in range(m)]

        for g in guards:
            grid[g[0]][g[1]] = 2

        for w in walls:
            grid[w[0]][w[1]] = 3

        for g in guards:
            self.dfs(g[0] - 1, g[1], grid, "U")
            self.dfs(g[0] + 1, g[1], grid, "D")
            self.dfs(g[0], g[1] - 1, grid, "L")
            self.dfs(g[0], g[1] + 1, grid, "R")

        out = 0
        for r in grid:
            out += r.count(0)
        return out
