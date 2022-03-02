"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []

        def dfs(pa, lst):
            if pa == None:
                return
            lst.append(pa.val)
            for ch in pa.children:
                dfs(ch, lst)
        dfs(root, ret)
        return ret
