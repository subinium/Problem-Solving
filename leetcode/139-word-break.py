class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordLen = list(map(len, wordDict))
        dp = [False for _ in range(n)]
        for idx in range(n):
            for word, l in zip(wordDict, wordLen):
                if idx+1 < l:
                    continue
                if (idx-l+1 == 0 or dp[idx-l]) and word == s[idx-l+1:idx+1]:
                    dp[idx] = True
                    break
        return dp[n-1]
