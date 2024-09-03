class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        maxx = float('-inf')

        for i in s:
            if i.isnumeric():
                if int(i) <= maxx:
                    return False
                maxx = int(i)
        return True