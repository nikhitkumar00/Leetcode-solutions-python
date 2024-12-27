class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur_max = 0
        cur = 0
        for value in values:
            cur -= 1
            if cur + value > cur_max:
                cur_max = cur + value
            if value > cur:
                cur = value
        return cur_max