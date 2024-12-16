class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))

        for _ in range(k):
            heappushpop(heap, (heap[0][0] * multiplier, heap[0][1]))

        return [i for i, j in sorted(heap, key=lambda x: x[1])]
