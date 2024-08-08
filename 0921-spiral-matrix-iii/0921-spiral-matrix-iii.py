class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row, col = rStart, cStart

        out = []
        steps = 1
        out.append([row, col])
        i = 0
        while len(out) < rows * cols:

            for _ in range(2):
                for _ in range(steps):
                    row, col = row + directions[i][0], col + directions[i][1]
                    if 0 <= row < rows and 0 <= col < cols:
                        out.append([row, col])
                i = (i + 1) % 4
            steps += 1

        return out
