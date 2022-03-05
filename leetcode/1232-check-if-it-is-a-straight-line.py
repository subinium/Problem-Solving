class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def comp(p1, p2, p3):
            return (p1[0]-p2[0])*(p2[1]-p3[1]) == (p1[1]-p2[1])*(p2[0]-p3[0])

        for idx in range(len(coordinates)):
            if idx < 2:
                continue
            if not comp(*coordinates[idx-2:idx+1]):
                return False

        return True
