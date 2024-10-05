class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = [0] * 26, [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            c1[ord(s1[i]) - 97] += 1
            c2[ord(s2[i]) - 97] += 1

        if c1 == c2:
            return True

        for i in range(len(s1), len(s2)):
            c2[ord(s2[i]) - 97] += 1
            c2[ord(s2[i - len(s1)]) - 97] -= 1

            if c1 == c2:
                return True

        return False
