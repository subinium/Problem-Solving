class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(map(lambda x: target in x, matrix))