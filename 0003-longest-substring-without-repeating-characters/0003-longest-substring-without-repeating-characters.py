class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        out = 0
        l = 0
        for i in s:
            while i in sett:
                sett.remove(s[l])
                l += 1
            sett.add(i)
            out = max(out, len(sett))
        return out
