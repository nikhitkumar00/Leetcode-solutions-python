class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0

        for _ in range(n - 1):
            
            next = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(next)

            if next == nums[i2] * 2:
                i2 += 1

            if next == nums[i3] * 3:
                i3 += 1

            if next == nums[i5] * 5:
                i5 += 1

        return nums[-1]
