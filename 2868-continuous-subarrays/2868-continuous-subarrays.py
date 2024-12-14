from sortedcontainers import SortedList


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        container = SortedList()
        out = 0
        l = 0

        for r in range(len(nums)):
            container.add(nums[r])

            while container[-1] - container[0] > 2:
                container.remove(nums[l])
                l += 1

            out += r - l + 1

        return out
