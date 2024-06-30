class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        out = []

        for char in s:
            if char.isnumeric() or ((char == "-" or char == "+") and len(out) == 0):
                out.append(char)
            else:
                break

        if len(out) <= 0:
            return 0

        out = "".join(out)

        if out == "-" or out == "+":
            return 0

        return max(min(int(out), 2**31 - 1), -(2**31))
