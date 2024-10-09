class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        b = 0
        out = 0
        for i in s:
            if i == "(":
                b += 1
            elif b != 0:
                b -= 1
            else:
                out += 1
        return out + b
