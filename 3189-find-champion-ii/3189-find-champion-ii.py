class Solution:
    def findChampion(self, n, edges):
        r = set(i[1] for i in edges)

        out = -1
        for i in range(n):
            if i not in r:
                if out == -1:
                    out = i
                else:
                    return -1
        return out
