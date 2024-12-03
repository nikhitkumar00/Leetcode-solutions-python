class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        for i in reversed(range(len(s))):
            arr.append(s[i])
            if spaces and spaces[-1] == i:
                arr.append(" ")
                spaces.pop()
        return "".join(reversed(arr))
