class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        cnt = 0
        while target > startValue:
            if target % 2:
                target += 1
            else:
                target //= 2
            cnt += 1

        return cnt+startValue-target
