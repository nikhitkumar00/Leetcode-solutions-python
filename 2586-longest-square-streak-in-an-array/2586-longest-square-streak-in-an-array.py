class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hashset = set(nums)
        streak = 0

        for num in nums:
            cur = 0
            temp = num

            while temp in hashset:
                cur += 1
                temp *= temp

            streak = max(streak, cur)

        return streak if streak > 1 else -1
