class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "({[":
                l.append(i)
            elif l and i in "]})":
                j = l[-1]
                if i == "]" and j == "[":
                    l.pop()
                elif i == "}" and j == "{":
                    l.pop()
                elif i == ")" and j == "(":
                    l.pop()
                else:
                    return False
            else:
                return False
        return False if l else True
