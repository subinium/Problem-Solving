# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.answer = -2e9

    def maxPath(self, root, idx):
        if root == None:
            return 0
        lmax = self.maxPath(root.left, idx*2+1)
        rmax = self.maxPath(root.right, idx*2+2)
        root.maxval = max([0, lmax, rmax]) + root.val
        answer = root.val
        if root.left:
            answer += max(0, root.left.maxval)
        if root.right:
            answer += max(0, root.right.maxval)
        self.answer = max(self.answer, answer)
        return root.maxval

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath(root, 0)
        return self.answer
