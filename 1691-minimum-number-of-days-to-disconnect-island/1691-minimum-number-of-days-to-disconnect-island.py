class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def dfs(i, j, visit):

            if (i, j) not in visit:
                visit.add((i, j))

                for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):

                    row, col = r + i, c + j
                    if (
                        0 <= row < len(grid)
                        and 0 <= col < len(grid[0])
                        and grid[row][col] == 1
                    ):
                        dfs(row, col, visit)

        def count_islands():

            visited = set()
            number_of_islands = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):

                    if (i, j) not in visited and grid[i][j] == 1:
                        dfs(i, j, visited)
                        number_of_islands += 1

            return number_of_islands

        if count_islands() != 1:
            return 0

        elif count_islands() == 1:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        if count_islands() != 1:
                            return 1
                        grid[i][j] = 1

        return 2
