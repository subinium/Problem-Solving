class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def singleSubseq(lst):
            n = len(lst)
            for i in range(3, n):
                lst[i] += max(lst[i-3], lst[i-2])
            return max(lst)

        answer = 0
        nums.sort()
        nums = nums+[0]
        stk, val, bf = [0], 0, 0

        for num in nums:
            if bf == num:
                val += num
            elif bf+1 == num:
                stk.append(val)
                val, bf = num, num
            else:
                stk.append(val)
                answer += singleSubseq(stk)
                stk, val, bf = [0], num, num

        return answer
