class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps, pos = 0, 0

        for i in range(len(s)):
            if s[i] == "0":
                swaps += i - pos
                pos += 1

        return swaps
