class Solution:

    def merge(self, low, mid, high):
        i = low
        j = mid + 1
        temp = []

        while i < mid+1 and j < high+1:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i < mid+1:
            temp.append(arr[i])
            i += 1
        
        while j < high+1:
            temp.append(arr[j])
            j += 1
        
        l = 0
        for i in range(low,high+1):
            arr[i] = temp[l]
            l += 1
        

    def mergesort(self, low, high):
        if low < high:

            mid = (low + high) // 2

            self.mergesort(low, mid)
            self.mergesort(mid + 1, high)
            self.merge(low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        global arr
        arr = []
        for i in nums:
            arr.append(i)
        self.mergesort(0, len(nums) - 1)
        return arr
