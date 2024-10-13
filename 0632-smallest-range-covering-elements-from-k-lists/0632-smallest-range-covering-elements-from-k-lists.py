class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize 'right' as the first number in the first list (nums[0][0])
        right = nums[0][0]
        # Initialize a min-heap (priority queue) to keep track of the smallest elements across lists
        heap = []

        # Iterate over each list in nums
        for i in range(len(nums)):
            # Update 'right' with the maximum first element of all lists
            right = max(right, nums[i][0])
            # Push the first element of each list into the heap, along with the list index (i) and the index of the element (0)
            heapq.heappush(
                heap,
                (
                    nums[i][0],
                    i,
                    0,
                ),  # (element, list index, element index within the list)
            )

        # 'left' will be the smallest element in the heap (the minimum of the first elements of all lists)
        left = heap[0][0]
        # Initialize the output range with [left, right] (the smallest and largest numbers so far)
        out = [left, right]

        # Keep iterating until we exhaust one of the lists
        while True:
            # Pop the smallest element from the heap (num is the smallest number)
            num, i, idx = heapq.heappop(heap)
            # Move to the next element in the same list (increment idx)
            idx += 1

            # If we have reached the end of the list, return the current smallest range (out)
            if idx == len(nums[i]):
                return out

            # Push the next element from the current list into the heap
            heapq.heappush(heap, (nums[i][idx], i, idx))
            # Update 'left' to the new smallest element in the heap
            left = heap[0][0]
            # Update 'right' if the new element is greater than the previous 'right'
            right = max(right, nums[i][idx])

            # If the new range (right - left) is smaller than the previous range, update the output range
            if right - left < out[1] - out[0]:
                out = [left, right]
