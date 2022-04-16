# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        val = 0
        def dfs(root):
            nonlocal val 
            if root==None: return 0
            dfs(root.right)
            root.val = val = val+root.val
            dfs(root.left)
        
        dfs(root)
        return root