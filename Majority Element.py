from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = dict(Counter(nums))

        max_freq = float("-inf")

        for i in c:
            if c[i] > max_freq:
                max_freq = c[i]
                max_ele = i

        return max_ele
