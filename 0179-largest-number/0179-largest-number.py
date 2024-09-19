class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        out = "".join(
            list(map(str, sorted(nums, reverse=True, key=lambda x: str(x) * 10)))
        )
        return out if int(out) != 0 else "0"
