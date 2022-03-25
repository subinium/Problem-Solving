# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        return (low<=root.val<=high) * root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)