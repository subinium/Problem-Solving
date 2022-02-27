# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        q = deque([[0, root]])
        while q:
            answer = max(answer, (q[-1][0]-q[0][0])+1)
            for _ in range(len(q)):
                j, node = q.popleft()
                if node.left:
                    q.append([j*2, node.left])
                if node.right:
                    q.append([(j*2)+1, node.right])
        return answer
