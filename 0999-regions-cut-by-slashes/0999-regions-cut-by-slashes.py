class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        main_grid = [[0 for _ in range(len(grid[0]) * 3)] for _ in range(len(grid) * 3)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                nr, nc = i * 3, j * 3

                if grid[i][j] == "/":
                    main_grid[nr][nc + 2] = 1
                    main_grid[nr + 1][nc + 1] = 1
                    main_grid[nr + 2][nc] = 1

                elif grid[i][j] == "\\":
                    main_grid[nr][nc] = 1
                    main_grid[nr + 1][nc + 1] = 1
                    main_grid[nr + 2][nc + 2] = 1

        count = 0
        visited = set()
        print(main_grid)

        def dfs(r, c):
            if (
                (r, c) not in visited
                and 0 <= r < len(main_grid)
                and 0 <= c < len(main_grid[0])
                and main_grid[r][c] != 1
            ):
                visited.add((r, c))

                dfs(r, c + 1)
                dfs(r, c - 1)
                dfs(r + 1, c)
                dfs(r - 1, c)

        for i in range(len(main_grid)):
            for j in range(len(main_grid[0])):

                if (i, j) not in visited and main_grid[i][j] != 1:

                    dfs(i, j)
                    count += 1

        return count
