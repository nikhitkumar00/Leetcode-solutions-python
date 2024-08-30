class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        # Define an "impossible" large value for edges that should not be used
        INF = int(2e9)

        # Initialize an adjacency list for the graph with n nodes
        graph = [[] for _ in range(n)]

        # Build the graph with the known weights
        for a, b, w in edges:
            if w != -1:  # Only add edges that have a known weight
                graph[a].append((b, w))
                graph[b].append((a, w))

        # Calculate the shortest path from source to destination using Dijkstra's algorithm
        current_distance = self.dijkstra(graph, source, destination)

        # If the current shortest distance is less than the target, it's impossible to reach the target distance
        if current_distance < target:
            return []

        # If the current shortest distance equals the target, set all unknown edges (-1) to a large value (INF)
        if current_distance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        # Try to adjust the edges with unknown weights to match the target distance
        for edge in edges:
            if edge[2] != -1:  # Skip edges that already have a known weight
                continue

            # Set the unknown edge's weight to 1 and update the graph
            edge[2] = 1
            graph[edge[0]].append((edge[1], 1))
            graph[edge[1]].append((edge[0], 1))

            # Recalculate the shortest path with the updated edge
            new_distance = self.dijkstra(graph, source, destination)

            # If the new distance is less than or equal to the target, adjust the edge weight
            if new_distance <= target:
                edge[2] += (
                    target - new_distance
                )  # Increase the edge weight to exactly match the target distance

                # Set all remaining unknown edges (-1) to a large value (INF)
                for i in edges:
                    if i[2] == -1:
                        i[2] = INF
                return edges

        # If no valid adjustment was found, return an empty list (no solution)
        return []

    def dijkstra(self, graph, source, destination):
        # Initialize the minimum distance to all nodes as infinity
        min_distance = [float("inf") for _ in graph]

        # The distance to the source node is 0
        min_distance[source] = 0

        # Initialize the priority queue (min-heap) with the source node and distance 0
        heap = [(0, source)]

        # While there are nodes to process in the heap
        while heap:
            # Pop the node with the smallest known distance
            distance, node = heapq.heappop(heap)

            # If this distance is already greater than the recorded minimum distance, skip it
            if distance > min_distance[node]:
                continue

            # Explore all neighbors of the current node
            for b, w in graph[node]:
                # If a shorter path to neighbor 'b' is found, update the distance and add it to the heap
                if distance + w < min_distance[b]:
                    min_distance[b] = distance + w
                    heapq.heappush(heap, (min_distance[b], b))

        # Return the shortest distance to the destination node
        return min_distance[destination]
