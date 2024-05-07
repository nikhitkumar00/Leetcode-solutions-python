def mostFrequentEven(self, nums):
    d = {}

    for i in nums:
        if i % 2 == 0:
            d[i] = d[i] + 1 if i in d else 1

    out = float("inf")
    maxx = 0
    for i in d:
        if d[i] > maxx:
            maxx = d[i]
            out = i
        elif d[i] == maxx and i < out:
            out = i

    return out if d or out != float("inf") else -1
