class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adj = [[i + 1] for i in range(n - 1)]
        out = []

        def shortest_path():
            q = deque([(0, 0)])  # node, len
            visit = set([(0, 0)])

            while q:
                node, length = q.popleft()
                if node == n - 1:
                    return length
                for nei in adj[node]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)

        for src, des in queries:
            adj[src].append(des)
            out.append(shortest_path())

        return out
