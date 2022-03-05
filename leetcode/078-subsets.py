class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ret = []
        for i in range(1 << l):
            tmp = []
            for j in range(l):
                if i & (1 << j):
                    tmp.append(nums[j])
            ret.append(tmp)
        return ret
