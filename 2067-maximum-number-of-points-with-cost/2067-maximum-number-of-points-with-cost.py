class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        left, right = [0] * COLS, [0] * COLS
        row = points[0]

        for i in range(1, ROWS):
            left[0] = row[0]
            right[-1] = row[-1]

            for l in range(1, COLS):
                left[l] = max(row[l], left[l - 1] - 1)

            for r in range(COLS - 2, -1, -1):
                right[r] = max(row[r], right[r + 1] - 1)

            for j in range(COLS):
                row[j] = max(left[j], right[j]) + points[i][j]
            print(row)

        return max(row)
