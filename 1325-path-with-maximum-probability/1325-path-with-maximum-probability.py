from collections import defaultdict
import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:

        # Create the graph as an adjacency list
        graph = defaultdict(list)

        # Build the graph with edges and corresponding success probabilities
        for index, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[index]))
            graph[b].append((a, succProb[index]))

        # A set to keep track of visited nodes
        visited = set()

        # Priority queue initialized with the starting node and a probability of 1
        pq = [(-1, start_node)]  # Negative because we are using min-heap as max-heap

        # While there are nodes to process in the priority queue
        while pq:
            probability, node = heapq.heappop(pq)

            # Mark the node as visited
            visited.add(node)

            # If we reach the end node, return the probability (negate it back)
            if node == end_node:
                return -probability

            # Process all adjacent nodes
            for nxt_node, nxt_probability in graph[node]:
                if nxt_node not in visited:
                    # Push the product of probabilities to the heap
                    heapq.heappush(pq, (probability * nxt_probability, nxt_node))

        # If the end node is not reachable, return 0
        return 0
