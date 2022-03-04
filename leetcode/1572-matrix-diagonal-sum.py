class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        n = len(mat)
        for i in range(n):
            answer += mat[i][i] + mat[i][n-i-1]
        return answer-n % 2*mat[n//2][n//2]
