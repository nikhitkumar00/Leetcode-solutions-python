class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        out = 0

        for i in range(rows - 2):
            for j in range(cols - 2):

                A, B, C = grid[i][j], grid[i][j + 1], grid[i][j + 2]
                D, E, F = grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2]
                G, H, I = grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]

                if (
                    max(A, B, C, D, E, F, G, H, I) > 9
                    or min(A, B, C, D, E, F, G, H, I) < 1
                    or len(set([A, B, C, D, E, F, G, H, I])) < 9
                ):
                    continue

                val = A + B + C
                if (
                    val == D + E + F
                    and val == G + H + I
                    and val == A + E + I
                    and val == C + E + G
                    and val == A + D + G
                    and val == B + E + H
                    and val == C + F + I
                ):
                    out += 1

        return out
