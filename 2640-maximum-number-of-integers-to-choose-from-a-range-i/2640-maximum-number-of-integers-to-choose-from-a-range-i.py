class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        out = 0
        cur_sum = 0
        for i in range(1,n+1):
            if i in banned:
                continue
            cur_sum += i
            if cur_sum > maxSum:
                break
            out += 1
        return out
