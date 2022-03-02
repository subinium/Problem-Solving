class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = min([abs(x-i)+abs(y-j)
                   for i, j in points if i == x or j == y]+[1e10])
        for idx, (i, j) in enumerate(points):
            if (x == i or y == j) and dist == abs(x-i)+abs(y-j):
                return idx
        return -1
