class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {x: i for i, x in enumerate(nums)}

        for i, x in enumerate(nums):
            if target - x in dic and i != dic[target - x]:
                return [i, dic[target - x]]
