class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0  # Initialize the index variable
        count = 0  # Initialize the count of elements not equal to val
        while i < len(nums):  # Iterate while index is within the range of nums
            if nums[i] == val:  # Check if current element is equal to the value to remove
                nums.pop(i)  # Remove the element
                continue  # Skip the increment of i to check the new element at current index
            count += 1  # Increment count for elements not equal to val
            i += 1  # Move to the next index
        return count  # Return the count of elements not equal to val