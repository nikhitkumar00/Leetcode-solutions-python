def convert(self, s: str, numRows: int) -> str:
    out = ""
    if numRows == 1:
        return s

    for i in range(numRows):
        inc = 2 * (numRows - 1)
        for j in range(i, len(s), inc):
            out += s[j]
            if i > 0 and i < numRows - 1 and j + inc - (2 * i) < len(s):
                out += s[j + inc - (2 * i)]
    return out
