class Solution:
    def splitListToParts(self, head, k):
        length = 0

        temp = head
        while temp:
            length += 1
            temp = temp.next

        out = []
        base = length // k
        rem = length % k
        cur_head = head

        for i in range(k):

            cur_length = base + (1 if i < rem else 0)

            if cur_head:
                out.append(cur_head)
                cur_length -= 1
            else:
                out.append(None)
                continue

            for _ in range(cur_length):
                if cur_head:
                    cur_head = cur_head.next
                    cur_length += 1

            if cur_head:
                prev = cur_head
                cur_head = cur_head.next
                prev.next = None

        return out
