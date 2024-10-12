class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals = sorted(intervals, key=lambda x: x[0])

        for start, end in intervals:
            if heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
