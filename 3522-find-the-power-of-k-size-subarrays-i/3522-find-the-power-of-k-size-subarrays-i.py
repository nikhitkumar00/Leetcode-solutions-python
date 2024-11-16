class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        out = []
        for i in range(len(nums) - k + 1):
            big = nums[i]
            for j in range(i + 1, i + k):
                if nums[j] != big + 1:
                    out.append(-1)
                    break
                else:
                    big = nums[j]
            else:
                out.append(big)

        return out
