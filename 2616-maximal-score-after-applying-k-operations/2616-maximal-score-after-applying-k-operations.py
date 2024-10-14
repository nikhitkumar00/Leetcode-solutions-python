class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-i for i in nums]
        heapq.heapify(nums)
        print(nums)

        for i in range(k):
            val = -heapq.heappop(nums)
            score += val
            heapq.heappush(nums, -ceil(val / 3))

        return score
