class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        maxi = swapi = swapj = -1
        maxx = "0"

        for i in reversed(range(len(num))):
            if num[i] > maxx:
                maxx, maxi = num[i], i

            if num[i] < maxx:
                swapi, swapj = i, maxi

        num[swapi], num[swapj] = num[swapj], num[swapi]
        return int("".join(num))
