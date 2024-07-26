from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums) -> int:
        dic = dict(Counter(nums))
        maxx = max(dic.values())

        count = 0
        for key in dic:
            if dic[key] == maxx:
                count += maxx

        return count
