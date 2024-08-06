from collections import Counter
import math


class Solution:
    def minimumPushes(self, word: str) -> int:

        c = Counter(word)
        arr = sorted(set(word), key=lambda x: c[x], reverse=True)

        count = 0
        for i in word:
            count += math.ceil((arr.index(i) + 1) / 8)

        return count
