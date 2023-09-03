class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {x: i for i, x in enumerate(nums)}
        for index, i in enumerate(nums):
            if target - i in dic and index != dic[target - i]:
                return [index, dic[target - i]]
