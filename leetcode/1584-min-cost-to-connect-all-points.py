class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v = len(points)
        edge = []
        for i in range(v):
            for j in range(i+1, v):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edge.append((i, j, dist))
        
        edge = sorted(edge, key=lambda x: x[2])
        parent = [i for i in range(v+1)]
        result = 0

        def find_(num):
            if num == parent[num] : return num
            parent[num] = find_(parent[num])
            return parent[num]

        def union_(a, b):
            if a < b : parent[a] = b
            else : parent[b] = a

        
        for st, ed, val in edge:
            v, w = find_(st), find_(ed)
            if v == w : continue
            union_(v, w)
            result += val

        
        
        return result
            
            