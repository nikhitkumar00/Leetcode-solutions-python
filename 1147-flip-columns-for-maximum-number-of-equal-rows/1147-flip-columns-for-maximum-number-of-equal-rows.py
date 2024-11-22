class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patFreq = defaultdict(int)

        for row in matrix:
            pattern = "".join(["T" if row[0] == i else "F" for i in row])
            patFreq[pattern] += 1

        return max(patFreq.values())
