class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row, col = rStart, cStart
        out = [[rStart, cStart]]
        steps = 1
        i = 0

        while len(out) < rows * cols:

            dr, dc = directions[i]
            for _ in range(steps):

                row, col = row + dr, col + dc
                if 0 <= row < rows and 0 <= col < cols:
                    out.append([row, col])

            i = (i + 1) % 4
            steps += 1 if i % 2 == 0 else 0

        return out
