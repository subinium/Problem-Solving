class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mn, mx = list(map(min, matrix)), list(map(max, zip(*matrix)))
        ret = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if mn[i] == mx[j] == val:
                    ret.append(val)
        return ret
