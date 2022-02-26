class Solution:
    def dfs(self, n, m, r, c, ck, image):
        ck[r][c] = 1
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(4):
            rr, cc = r+dx[i], c+dy[i]
            if not (0 <= rr < n and 0 <= cc < m):
                continue
            if ck[rr][cc] or image[r][c] != image[rr][cc]:
                continue
            self.dfs(n, m, rr, cc, ck, image)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        ck = [[0 for _ in range(m)] for _ in range(n)]
        self.dfs(n, m, sr, sc, ck, image)
        for i in range(n):
            for j in range(m):
                if ck[i][j]:
                    image[i][j] = newColor
        return image
