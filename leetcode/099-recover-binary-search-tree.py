# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        idx, lst = 0, []
        def dfs(root):
            if root==None: return
            dfs(root.left)
            lst.append(root.val)
            dfs(root.right)
            
        def dfs2(root):
            nonlocal idx
            if root==None: return
            dfs2(root.left)
            root.val = lst[idx]
            idx += 1
            dfs2(root.right)
        
        dfs(root)
        lst.sort()
        dfs2(root)
        