class Solution:
    def maximumLength(self, s: str) -> int:
        out = -1

        for i in range(1, len(s) + 1):
            counter = defaultdict(int)

            for j in range(len(s) - i + 1):
                sub = s[j : j + i]

                if len(set(sub)) == 1:
                    counter[sub] += 1

                    if counter[sub] >= 3:
                        out = max(out, i)

        return out
