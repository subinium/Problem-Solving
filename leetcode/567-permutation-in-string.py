class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        cnt1, cnt2 = [[0 for _ in range(26)] for _ in range(2)]
        for c1, c2 in zip(s1, s2):
            cnt1[ord(c1)-ord('a')] += 1
            cnt2[ord(c2)-ord('a')] += 1

        if cnt1 == cnt2:
            return True

        for i in range(l1, l2):
            cnt2[ord(s2[i-l1])-ord('a')] -= 1
            cnt2[ord(s2[i])-ord('a')] += 1
            if cnt1 == cnt2:
                return True

        return False
