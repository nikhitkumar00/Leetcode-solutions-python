class Solution:
    def makeFancyString(self, s: str) -> str:
        out = []

        if len(s) < 3:
            return s

        out.append(s[0])
        out.append(s[1])

        for i in range(2, len(s)):
            if s[i] == out[-1] == out[-2]:
                continue
            out.append(s[i])

        return "".join(out)
