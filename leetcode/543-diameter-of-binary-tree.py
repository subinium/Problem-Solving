# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            depth = max(dfs(root.left), dfs(root.right))+1
            root.depth = depth
            return root.depth

        def dfs2(root):
            if not root:
                return 0
            d = 0
            if root.left:
                d += root.left.depth
            if root.right:
                d += root.right.depth
            return max(d, dfs2(root.left), dfs2(root.right))

        dfs(root)
        return dfs2(root)
