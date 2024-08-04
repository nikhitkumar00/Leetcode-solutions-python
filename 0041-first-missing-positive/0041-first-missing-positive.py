class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        sett = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in sett:
                return i

        # # Replace all negative numbers with 0, since we are only interested in positive numbers
        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         nums[i] = 0

        # # Use the index as a hash key to mark the presence of a number
        # for i in range(len(nums)):
        #     val = abs(nums[i])
        #     # Check if the value is within the range of the array
        #     if 1 <= val <= len(nums):
        #         # If the value at the indexed position is 0, mark it as negative to indicate presence
        #         if nums[val - 1] == 0:
        #             nums[val - 1] = (len(nums) + 1) * -1
        #         # If the value at the indexed position is positive, make it negative to indicate presence
        #         if nums[val - 1] > 0:
        #             nums[val - 1] *= -1

        # # Find the first index with a non-negative value, which indicates the first missing positive number
        # for i in range(len(nums)):
        #     if nums[i] >= 0:
        #         return i + 1

        # # If no missing positive number is found within the range, return the length of the array + 1
        # return len(nums) + 1
