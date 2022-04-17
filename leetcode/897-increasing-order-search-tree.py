# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def dfs(root):
            if root==None: return 
            dfs(root.left)
            lst.append(TreeNode(root.val))
            dfs(root.right)
        
        dfs(root)
        if not lst: return
        for i in range(len(lst)-1): lst[i].right = lst[i+1]
        return lst[0]