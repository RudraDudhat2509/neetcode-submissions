# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def kth(self,head,k):
        while head and k>0:
            head=head.next
            k-=1
        return head 
    def reverse_group(self,start,stop):
        prev=stop
        curr=start
        while curr!=stop:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        while True:
            kth_node=self.kth(prev,k)
            if not kth_node:
                break
            gnext=kth_node.next
            gfirst=prev.next
            self.reverse_group(gfirst,gnext)
            prev.next=kth_node
            prev=gfirst
        return dummy.next