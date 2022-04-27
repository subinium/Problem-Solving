class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(now):
            if group[now]: return
            group[now] = True
            sub.append(now)
            for nxt in lst[now]:
                dfs(nxt)
        
        n = len(s)
        lst, group = [[] for _ in range(n)], [False for _ in range(n)]
        sub, ret = [], [None for _ in range(n)]
        
        for x, y in pairs:
            lst[x].append(y)
            lst[y].append(x)
            
        for i in range(n):
            if group[i]: continue
            dfs(i)
            sub.sort()
            substr = sorted(''.join([s[idx] for idx in sub]))
            for idx, val in enumerate(sub): ret[val] = substr[idx]
            sub = []
        
        return ''.join(ret)