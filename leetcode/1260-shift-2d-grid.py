class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        sz = n*m
        grid2 = deepcopy(grid)
        for i in range(n):
            for j in range(m):
                ii, jj = divmod((i*m+j+k)%sz, m)
                grid2[ii][jj] = grid[i][j]
        return grid2