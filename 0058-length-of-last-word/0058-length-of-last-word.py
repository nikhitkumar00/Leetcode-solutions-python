class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in reversed(s.split(' ')):
            if len(i) > 0:
                return len(i)
            continue