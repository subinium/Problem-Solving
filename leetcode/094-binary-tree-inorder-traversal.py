# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, lst):
            if not node:
                return
            dfs(node.left, lst)
            lst.append(node.val)
            dfs(node.right, lst)

        ret = []
        dfs(root, ret)
        return ret
