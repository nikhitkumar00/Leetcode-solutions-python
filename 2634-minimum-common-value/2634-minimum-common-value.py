class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1).intersection(set(nums2))) if set(nums1).intersection(set(nums2)) else -1