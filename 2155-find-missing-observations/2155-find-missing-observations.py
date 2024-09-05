class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = (mean * (len(rolls) + n)) - sum(rolls)

        if tot < n or tot > 6 * n:
            return []

        base = tot // n
        remainder = tot % n

        out = [base] * n
        for i in range(remainder):
            out[i] += 1

        return out
