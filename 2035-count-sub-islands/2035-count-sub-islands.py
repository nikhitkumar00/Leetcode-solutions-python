class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def dfs(i, j):
            # Check if the current cell is within bounds and is part of an island in grid2
            if (
                0 <= i < len(grid2)  # Check row boundaries
                and 0 <= j < len(grid2[0])  # Check column boundaries
                and grid2[i][j] == 1  # Check if the cell is part of an island in grid2
            ):
                # Assume the current island in grid2 is a sub-island of grid1
                is_sub = True

                # Mark the current cell in grid2 as visited by setting it to 0
                grid2[i][j] = 0

                # If the corresponding cell in grid1 is not part of an island, mark it as not a sub-island
                if grid1[i][j] != 1:
                    is_sub = False

                # Recursively check all four directions (down, up, right, left)
                is_sub = dfs(i + 1, j) and is_sub  # Down
                is_sub = dfs(i - 1, j) and is_sub  # Up
                is_sub = dfs(i, j + 1) and is_sub  # Right
                is_sub = dfs(i, j - 1) and is_sub  # Left

                # Return True if all parts of the island in grid2 correspond to parts of an island in grid1
                return is_sub

            # Return True for out-of-bounds or already visited cells, as they don't affect the sub-island status
            return True

        count = 0

        # Iterate through each cell in grid2
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):

                # If the cell in grid2 is part of an island and hasn't been visited
                if grid2[i][j] == 1:
                    # Perform DFS to determine if the island is a sub-island
                    if dfs(i, j):
                        count += 1  # Increment the sub-island count if it is a sub-island

        # Return the total count of sub-islands
        return count
