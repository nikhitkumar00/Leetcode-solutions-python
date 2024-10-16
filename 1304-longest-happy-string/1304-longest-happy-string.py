class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        aa, bb, cc, total = 0, 0, 0, a + b + c
        out = []

        for i in range(total):
            if (a >= b and a >= c and aa != 2) or (a > 0 and (bb == 2 or cc == 2)):
                out.append("a")
                a -= 1
                aa += 1
                bb, cc = 0, 0
            elif (b >= a and b >= c and bb != 2) or (b > 0 and (aa == 2 or cc == 2)):
                out.append("b")
                b -= 1
                bb += 1
                aa, cc = 0, 0
            elif (c >= b and c >= a and cc != 2) or (c > 0 and (bb == 2 or aa == 2)):
                out.append("c")
                c -= 1
                cc += 1
                bb, aa = 0, 0
        return "".join(out)
