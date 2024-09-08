class Solution:
    def splitListToParts(self, head, k):
        # Step 1: Calculate the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Step 2: Determine the base size and remainder
        base = length // k
        rem = length % k
        
        # Step 3: Initialize output list and current pointer
        result = []
        cur_head = head

        for i in range(k):
            # Calculate the size of the current part
            cur_size = base + (1 if i < rem else 0)
            part_head = cur_head

            # Traverse cur_size elements
            for j in range(cur_size - 1):
                if cur_head:
                    cur_head = cur_head.next

            # Break the link after cur_size elements
            if cur_head:
                next_part = cur_head.next
                cur_head.next = None
                cur_head = next_part

            # Append the current part head to result
            result.append(part_head)

        return result
