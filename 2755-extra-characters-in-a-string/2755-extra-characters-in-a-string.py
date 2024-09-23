class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        words = set(dictionary)
        cache = {len(s):0}

        def dp(start):
            if start in cache:
                return cache[start]

            cache[start] = 1 + dp(start + 1)

            for end in range(start, len(s)):
                if s[start : end + 1] in words:
                    cache[start] = min(cache[start], dp(end + 1))

            return cache[start]

        return dp(0)
