class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        out = []

        adj = defaultdict(deque)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for start, end in pairs:
            adj[start].append(end)
            indegree[end] += 1
            outdegree[start] += 1

        start_node = -1
        for start in outdegree:
            if outdegree[start] == indegree[start] + 1:
                start_node = start
                break
        start_node = pairs[0][0] if start_node == -1 else start_node

        def visit(node):
            while adj[node]:
                visit(adj[node].popleft())
            out.append(node)
        
        visit(start_node)

        return [[out[i], out[i-1]] for i in reversed(range(1,len(out)))]