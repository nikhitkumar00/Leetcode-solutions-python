class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0

        cur = 0
        dic = {0: -1}
        res = len(nums)

        for i, n in enumerate(nums):
            cur = (cur + n) % p
            prefix = (cur - remainder + p) % p
            if prefix in dic:
                res = min(res, i - dic[prefix])
                if res == 1:
                    return 1
            dic[cur] = i

        return -1 if res == len(nums) else res
