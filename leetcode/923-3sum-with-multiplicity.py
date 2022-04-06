class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        def comb(x, n):
            if x<n: return 0
            ret = 1
            for i in range(n): ret = ret*(x-i)//(i+1)
            return ret
            
        ret = 0
        cnt = Counter(arr)
        for a in range(101):
            for b in range(a, 101):
                c = target-a-b
                if c<b: break
                if a==b==c: ret += comb(cnt[a], 3)
                elif a==b: ret += comb(cnt[a], 2)*cnt[c]
                elif b==c: ret += comb(cnt[b], 2)*cnt[a]
                else: ret += cnt[a]*cnt[b]*cnt[c]
                
        return ret%int(1e9+7)