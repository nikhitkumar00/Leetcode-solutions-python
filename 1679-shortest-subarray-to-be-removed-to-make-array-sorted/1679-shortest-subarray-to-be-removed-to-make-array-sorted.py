class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1

        out = r
        while l < r and (l == 0 or arr[l] >= arr[l - 1]):
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            out = min(out, r - l - 1)
            l += 1
        return out