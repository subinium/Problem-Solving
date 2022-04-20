# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = -1
        self.lst = []
        def dfs(root):
            if root==None: return 
            dfs(root.left)
            self.lst.append(root.val)
            dfs(root.right)
        dfs(root)
            
            
    def next(self) -> int:
        self.idx+=1
        return self.lst[self.idx]

    def hasNext(self) -> bool:
        return self.idx+1 < len(self.lst)
        