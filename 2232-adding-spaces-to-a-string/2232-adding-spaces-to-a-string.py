class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        i = 0

        for space in spaces:
            arr.append(s[i:space])
            i = space
        arr.append(s[i:])

        return " ".join(arr)
