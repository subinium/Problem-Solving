class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        for cs in zip(*strs):
            if len(set(cs)) > 1:
                break
            answer += cs[0]
        return answer
