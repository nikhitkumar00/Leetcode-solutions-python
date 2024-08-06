from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:

        n = sorted(Counter(word).values(), reverse=True)
        return sum(n[i] * ((i // 8) + 1) for i in range(len(n)))
