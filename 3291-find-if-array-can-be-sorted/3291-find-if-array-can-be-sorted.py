class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        curmax = curmin = nums[0]
        prevbit = nums[0].bit_count()
        temp = []

        for i in nums:
            if prevbit == i.bit_count():
                curmax, curmin = max(i, curmax), min(i, curmin)
            else:
                temp.append((curmax, curmin))
                curmax = curmin = i
                prevbit = i.bit_count()
        temp.append((curmax, curmin))

        for i in range(1, len(temp)):
            if temp[i][1] < temp[i - 1][0]:
                return False
        return True
