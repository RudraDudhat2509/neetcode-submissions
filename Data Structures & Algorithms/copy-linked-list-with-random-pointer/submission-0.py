"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={None: None}
        root=head 
        while root: 
            if root not in dic: 
                dic[root]=Node(root.val)
            root=root.next
        root=head
        while root:
            copy=dic[root] 
            copy.next=dic[root.next]
            copy.random=dic[root.random]
            root=root.next
        return dic[head]