class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def dfs(arr, visit, i, j):
            stack = [(i, j)]
            d = ((0, 1), (0, -1), (1, 0), (-1, 0))
            temp = set()
            
            while stack:
                
                r, c = stack.pop()
                visit.add((r, c))
                temp.add((r, c))

                
                for dr, dc in d:
                    
                    row, col = r + dr, c + dc
                    if (
                        0 <= row < len(arr)
                        and 0 <= col < len(arr[0])
                        and arr[row][col] == 1
                        and (row, col) not in visit
                    ):
                        stack.append((row, col))

            return temp

        
        visit = set()
        count = 0

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):

                if (i, j) not in visit and grid2[i][j] == 1:
                    for r, c in dfs(grid2, visit, i, j):
                        if grid1[r][c] != 1:
                            break
                    else:
                        count += 1
        
        return count
