class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def calc(n):
            return (n-2)*(n-1)//2

        ret = 0
        nums += [4000]
        st, cnt, d = 4000, 1, 4000

        for num in nums:
            if st-num == d:
                cnt += 1
            else:
                ret += calc(cnt)
                cnt = 2
            st, d = num, st-num

        return ret
