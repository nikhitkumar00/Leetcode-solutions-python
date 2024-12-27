class Solution:
    def maxScoreSightseeingPair(self, values):
        max_left = values[0]
        cur_max = 0

        for i in range(1, len(values)):
            cur_val = values[i] - i

            cur_max = max(cur_max, max_left + cur_val)
            max_left = max(max_left, values[i] + i)

        return cur_max
