class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        st, ed = None, None
        for idx, (x, y) in enumerate(zip(nums, nums_sorted)):
            if x==y: continue
            if st==None: st = idx
            ed = idx
        
        return ed-st+1 if ed!=None else 0