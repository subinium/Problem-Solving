class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(st):
            now, c = [st], 0
            ck[st] = c

            while now:
                c ^=1
                nxt = []
                for i in now:
                    for j in graph[i]:
                        if ck[j]!=None: continue
                        ck[j] = c
                        nxt.append(j)
                now = nxt
        
        n = len(graph)
        ck = [None for _ in range(n)]
        for i in range(n):
            if ck[i]==None: bfs(i)

        for idx, val in enumerate(graph):
            for jdx in val:
                if ck[idx]==ck[jdx]: return False
        
        return True