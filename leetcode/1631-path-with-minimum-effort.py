class Solution:
    def check(self, heights, diff):
        n, m = len(heights), len(heights[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        ck = [[True for _ in range(m)] for _ in range(n)]
        now = [(0, 0)]
        ck[0][0] = False
        while now:
            nxt = []
            for x, y in now:
                if x==n-1 and y==m-1: return True
                for xx, yy in zip(dx, dy):
                    nx, ny = x+xx, y+yy
                    if 0<=nx<n and 0<=ny<m and ck[nx][ny] and abs(heights[nx][ny]-heights[x][y])<=diff: 
                        nxt.append((nx, ny))
                        ck[nx][ny] = False    
            now = nxt
        return False
            
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        lo, hi = 0, 1000000
        while lo < hi:
            mid = (lo+hi)//2
            if self.check(heights, mid): hi = mid
            else: lo = mid+1
        return hi