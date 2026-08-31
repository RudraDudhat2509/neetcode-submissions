# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildheap(self,root,heap):
        if(root is None):
            return None
        heapq.heappush(heap,-root.val)
        self.buildheap(root.left,heap)
        self.buildheap(root.right,heap)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        self.buildheap(root,heap)
        while(len(heap)!=k):
            heapq.heappop(heap)
        return -heap[0]
        