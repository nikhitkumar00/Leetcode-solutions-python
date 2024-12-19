class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        out = 0
        curmax = -1
        for i, n in enumerate(arr):
            curmax = max(curmax, n)
            if curmax <= i:
                out += 1
        return out
