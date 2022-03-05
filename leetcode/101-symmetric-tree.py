# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            vals = [node.val if node else None for node in queue]
            if vals != vals[::-1]:
                return False
            new_queue = []
            for node in queue:
                if not node:
                    continue
                new_queue.append(node.left)
                new_queue.append(node.right)
            queue = new_queue
        return True
