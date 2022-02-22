class Solution:
    def __init__(self):
        self.ret = []

    def dfs(self, s, l, r, n):
        if len(s) == 2*n:
            self.ret.append(s)
            return
        if l < n:
            self.dfs(s+'(', l+1, r, n)
        if l > r:
            self.dfs(s+')', l, r+1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs('', 0, 0, n)
        return self.ret
