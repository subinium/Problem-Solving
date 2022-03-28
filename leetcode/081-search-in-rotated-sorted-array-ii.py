class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bs(st, ed):
            if ed - st <= 1: return target in nums[st: ed+1]
            mid = (st+ed)//2
            if nums[mid] == nums[ed]: return bs(mid+1, ed) or bs(st, mid)
            
            if nums[mid] > nums[ed]:
                if nums[ed] < target <= nums[mid]: ed = mid
                else: st = mid+1
            else:
                if nums[mid] < target <= nums[ed]: st = mid+1
                else: ed = mid
                    
            return bs(st, ed)
        
        return bs(0, len(nums)-1)