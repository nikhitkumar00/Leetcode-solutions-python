class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp = head

        while head and head.next:
            head.next = ListNode(gcd(head.val, head.next.val), head.next)
            head = head.next.next

        return temp