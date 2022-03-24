class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        answer = []
        if ls<lp: return answer
        alps = string.ascii_lowercase
        ds, dp = {c:0 for c in alps}, {c:0 for c in alps}
        for cs, cp in zip(s[:lp], p):
            ds[cs]+=1
            dp[cp]+=1
        ret = []
        for idx in range(ls-lp+1):    
            if ds==dp: ret.append(idx)
            ds[s[idx]]-=1
            ds[s[idx+lp]]+=1
        if ds==dp: ret.append(ls-lp)
        return ret
        