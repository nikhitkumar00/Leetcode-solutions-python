class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        for i in s:
            if i == "[":
                unbalanced += 1
            elif unbalanced:
                unbalanced -= 1

        return (unbalanced + 1) // 2
