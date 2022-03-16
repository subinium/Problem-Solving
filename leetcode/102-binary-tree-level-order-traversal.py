# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        ret = []
        while queue:
            vals, new_queue = [], []
            for node in queue:
                if not node:
                    continue
                vals.append(node.val)
                new_queue.append(node.left)
                new_queue.append(node.right)
            if vals:
                ret.append(vals)
            queue = new_queue
        return ret
