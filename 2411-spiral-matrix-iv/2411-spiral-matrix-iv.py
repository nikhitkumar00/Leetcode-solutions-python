# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m, n, head):
        d = ((0, 1), (1, 0), (0, -1), (-1, 0))
        out = [[-1] * n for _ in range(m)]

        i = 0
        r, c = 0, 0

        while head:
            print(head.val, d[i], r, c)
            out[r][c] = head.val
            r, c = r + d[i][0], c + d[i][1]
            if r < 0 or r >= m or c < 0 or c >= n or out[r][c] != -1:
                r, c = r - d[i][0], c - d[i][1]
                i = (i + 1) % 4
                r, c = r + d[i][0], c + d[i][1]

            head = head.next

        return out
