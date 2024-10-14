class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-i for i in nums]
        heapq.heapify(nums)

        for i in range(k):
            score -= heapq.heappushpop(nums, floor(nums[0] / 3))

        return score
