class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]
        idx = 1
        while idx <= query_row:
            nxt = [0.0]*(idx+1)
            for j in range(idx):
                if curr[j]>=1:   
                    nxt[j]+=(curr[j]-1)/2
                    nxt[j+1]+=(curr[j]-1)/2
            idx, curr = idx+1, nxt
        
        return min(curr[query_glass], 1)