class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = {}
        for i in text:
            if i in c:
                c[i] += 1
            elif i in ("b","a","l","o","n"):
                c[i] = 1
        out = 0
        while True:
            for i in "balloon":
                if i in c and c[i] > 0:
                    c[i] -= 1
                else:
                    return out
            out += 1