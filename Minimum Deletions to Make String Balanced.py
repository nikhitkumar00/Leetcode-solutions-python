class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        temp = [[0, 0] for i in range(n)]
        cur_a = s.count("a")
        cur_b = 0
        smallest = float("inf")

        for i in range(n):
            temp[i][0] = cur_b

            if s[i] == "b":
                cur_b += 1
            else:
                cur_a -= 1

            temp[i][1] = cur_a

            if temp[i][0] + temp[i][1] < smallest:
                smallest = temp[i][0] + temp[i][1]

        return smallest
