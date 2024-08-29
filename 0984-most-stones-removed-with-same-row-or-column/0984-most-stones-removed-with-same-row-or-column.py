class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        connected = 0
        visit = set()

        def checker(i, j):
            for r, c in stones:
                if (r, c) not in visit and (i == r or j == c):
                    visit.add((r, c))
                    checker(r, c)

        for row, col in stones:
            if (row, col) not in visit:
                checker(row, col)
                connected += 1

        return len(stones) - connected
