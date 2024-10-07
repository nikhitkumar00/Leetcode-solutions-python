class Solution:
    def minLength(self, s: str) -> int:
        flag = True
        while flag:
            flag = False
            for i in range(len(s)-1):
                if s[i:i+2] in ("AB","CD"):
                    s = s[:i]+s[i+2:]
                    flag = True
        return len(s)