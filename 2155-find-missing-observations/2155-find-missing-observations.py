class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = (mean * (len(rolls) + n)) - sum(rolls)

        if tot < n or tot > 6 * n:
            return []

        base = tot // n
        remainder = tot % n

        return [base + (1 if i < remainder else 0) for i in range(n)]
