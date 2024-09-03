# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        while l1 != None:
            num1.append(l1.val)
            l1 = l1.next
        
        num2 = []
        while l2 != None:
            num2.append(l2.val)
            l2 = l2.next
        
        num1.reverse()
        num2.reverse()
        num1 = int("".join(list(map(str,num1))))
        num2 = int("".join(list(map(str,num2))))
        
        summ = num1 + num2
        
        result = None
        for i in str(summ):
            newnode = ListNode(val = int(i), next = None)
            newnode.next = result
            result = newnode
        return result
