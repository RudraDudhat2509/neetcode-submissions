# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def make_number(self, l1) -> int:
        result=0
        m=1
        while l1:
            result=result+m*l1.val
            m*=10
            l1=l1.next
        return result

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = self.make_number(l1) + self.make_number(l2)
        if num == 0:
            return ListNode(0)
            
        head = ListNode(num % 10)
        num //= 10  # Use integer division
        tail = head
        
        while num > 0:
            tail.next = ListNode(num % 10)
            tail = tail.next
            num //= 10  # Use integer division

        return head
