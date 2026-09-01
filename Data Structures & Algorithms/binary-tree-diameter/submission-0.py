# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxd(self,root):
        if root is None:
            return 0 
        return 1+ max(self.maxd(root.left),self.maxd(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0 
        left=self.maxd(root.left)
        right=self.maxd(root.right)
        through=left+right
        leftd=self.diameterOfBinaryTree(root.left)
        rightd=d=self.diameterOfBinaryTree(root.right)
        return max(through,leftd,rightd)