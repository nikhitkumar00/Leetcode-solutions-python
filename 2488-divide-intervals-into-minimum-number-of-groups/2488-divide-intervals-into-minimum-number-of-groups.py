class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = sorted([i[0] for i in intervals]), sorted([i[1] for i in intervals])

        i, j, out = 0, 0, 0
        while i < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1

            out = max(out, i - j)

        return out
