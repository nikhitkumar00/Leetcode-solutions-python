class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        hashset = set()

        def dfs(i):
            if i == len(s):
                return 0

            out = 0
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if sub not in hashset:
                    hashset.add(sub)
                    out = max(out, 1 + dfs(j + 1))
                    hashset.remove(sub)
            return out

        return dfs(0)
