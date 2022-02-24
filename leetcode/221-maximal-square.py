class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j]:
                    matrix[i][j] = min(
                        [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]])+1

        return max([max(row) for row in matrix])**2
