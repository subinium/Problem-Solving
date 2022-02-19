class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[None for _ in range(n)] for _ in range(n)]
        vx, vy = [0, 1, 0, -1], [1, 0, -1, 0]
        way, sx, sy = 0, 0, 0
        for i in range(1, n*n+1):
            ret[sx][sy] = i
            nx, ny = sx+vx[way], sy+vy[way]
            if not (0 <= nx < n and 0 <= ny < n) or ret[nx][ny]:
                way = (way+1) % 4
                nx, ny = sx+vx[way], sy+vy[way]
            sx, sy = nx, ny
        return ret
