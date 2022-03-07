# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], lr=None) -> int:
        if root == None:
            return 0
        if lr == True and root.left == root.right == None:
            return root.val
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
