class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        r, c = [False for _ in range(n)], [False for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    r[i] = c[j] = True
        for i in range(n):
            for j in range(m):
                if r[i] or c[j]:
                    matrix[i][j] = 0
