class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix2 = list(map(lambda x: list(x[::-1]), zip(*matrix)))
        matrix[:] = matrix2
