class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ret = 0
        for key, val in cnt.items():
            if val==0: continue
            if key*2==k: continue
            ret += min(val, cnt.get(k-key,0))
        return ret//2 + (k%2==0)*(cnt.get(k//2, 0)//2)