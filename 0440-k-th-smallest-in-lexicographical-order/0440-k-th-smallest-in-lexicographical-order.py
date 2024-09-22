class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k > 0:
            steps = self.count(n, cur, cur + 1)

            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1

        return cur

    def count(self, n, p1, p2):
        steps = 0

        while p1 <= n:
            steps += min(n + 1, p2) - p1
            p1 *= 10
            p2 *= 10

        return steps
