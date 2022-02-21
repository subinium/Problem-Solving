class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i]*nums[i+1] <= 0:
                break
        else:
            i = n*(nums[-1] < 0)-1

        ret = []
        p1, p2 = i, i+1
        while 0 <= p1 or p2 < n:
            if p2 == n or 0 <= p1 and nums[p1]**2 < nums[p2]**2:
                ret.append(nums[p1]**2)
                p1 -= 1
            else:
                ret.append(nums[p2]**2)
                p2 += 1

        return ret
