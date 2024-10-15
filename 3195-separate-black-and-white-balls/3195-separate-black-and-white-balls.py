class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps, out = 0, 0

        for i in s:
            if i == "1":
                swaps += 1
            else:
                out += swaps

        return out
