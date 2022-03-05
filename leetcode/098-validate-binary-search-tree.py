# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = []

        def dfs(node, lst):
            if not node:
                return
            dfs(node.left, lst)
            ret.append(node.val)
            dfs(node.right, lst)

        dfs(root, ret)
        for i in range(1, len(ret)):
            if ret[i-1] >= ret[i]:
                return False
        return True
