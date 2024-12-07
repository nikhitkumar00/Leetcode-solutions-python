class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            ops = 0
            for num in nums:
                ops += ceil(num / m) - 1
                if ops > maxOperations:
                    break
            if ops <= maxOperations:
                r = m
            else:
                l = m + 1
        return l
