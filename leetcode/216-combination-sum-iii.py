class Solution:
    def __init__(self):
        self.answer = []

    def dfs(self, lst, remain, k):
        st = lst[-1] if lst else 0
        if len(lst) == k-1 and remain > st and remain < 10:
            self.answer.append(lst+[remain])
            return

        for i in range(st+1, 10):
            if 2*i+1 > remain:
                break
            self.dfs(lst+[i], remain-i, k)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.dfs([], n, k)
        return self.answer
