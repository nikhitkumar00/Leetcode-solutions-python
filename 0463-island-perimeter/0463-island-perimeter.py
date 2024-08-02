class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1),(0, -1),(1, 0),(-1, 0))
        out = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    perimeter = 4

                    for row, col in directions:
                        r, c = i + row, j + col

                        if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                            perimeter -= 1

                    out += perimeter
                    
        return out