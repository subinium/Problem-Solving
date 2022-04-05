class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        st, ed = 0, len(height)-1
        while st < ed:
            if height[st] < height[ed]:
                mx = max(mx, (ed-st)*height[st])
                st += 1
            else:
                mx = max(mx, (ed-st)*height[ed])
                ed -= 1
        return mx