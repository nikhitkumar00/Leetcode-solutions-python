class Solution:
    def clearDigits(self, s: str) -> str:
        changed = True
        while changed:
            changed = False
            for i in range(len(s)):
                if s[i].isdigit():
                    s = s[: i - 1] + s[i + 1 :]
                    changed = True
                    break
        return s
