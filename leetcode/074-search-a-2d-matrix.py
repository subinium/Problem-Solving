# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for row in matrix:
#             for val in row:
#                 if val == target:
#                     return True
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any([target in row for row in matrix])
                        