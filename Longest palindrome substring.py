class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        maxx = 0

        def checking():
            nonlocal out, maxx, l, r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > maxx:
                    out = s[l : r + 1]
                    maxx = length
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i
            checking()

            l, r = i, i + 1
            checking()

        return out
