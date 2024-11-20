class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]  # a, b, c

        for char in s:
            count[ord(char) - ord("a")] += 1

        if min(count) < k:
            return -1

        out = inf
        l = r = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord("a")] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord("a")] += 1
                l += 1

            out = min(out, len(s) - (r - l + 1))
        return out
