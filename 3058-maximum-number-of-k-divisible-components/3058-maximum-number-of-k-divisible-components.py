class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(cur, parent):
            total = values[cur]
            for child in adj[cur]:
                if child != parent:
                    total += dfs(child, cur)

            if total % k == 0:
                nonlocal out
                out += 1

            return total

        out = 0
        dfs(0, -1)
        return out
