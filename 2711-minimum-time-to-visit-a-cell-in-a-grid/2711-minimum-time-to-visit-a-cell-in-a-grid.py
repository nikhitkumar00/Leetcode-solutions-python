class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        heap = [(0, 0, 0)]  # time, row, col
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        while heap:
            t, r, c = heapq.heappop(heap)
            directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))

            if r == ROWS - 1 and c == COLS - 1:
                return t

            for nr, nc in directions:
                if (
                    nr < 0
                    or nc < 0
                    or nr == ROWS
                    or nc == COLS
                    or (nr, nc) in visit
                ):
                    continue

                wait = 0 if abs(grid[nr][nc] - t) % 2 else 1
                new_time = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(heap, (new_time, nr, nc))
                visit.add((nr, nc))
