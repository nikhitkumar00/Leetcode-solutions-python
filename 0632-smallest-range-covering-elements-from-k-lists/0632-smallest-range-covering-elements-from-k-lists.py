class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        right = nums[0][0]
        heap = []

        for i in range(len(nums)):
            right = max(right, nums[i][0])
            heapq.heappush(
                heap, (nums[i][0], i, 0)
            )  # num, idx in nums, idx of num in nums[0]

        left = heap[0][0]
        out = [left, right]

        while True:
            num, i, idx = heapq.heappop(heap)
            idx += 1

            if idx == len(nums[i]):
                return out

            heapq.heappush(heap, (nums[i][idx], i, idx))
            left = heap[0][0]
            right = max(right, nums[i][idx])

            if right - left < out[1] - out[0]:
                out = [left, right]
