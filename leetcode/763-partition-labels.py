# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         st, ed = 0, 0
#         ret = []
#         for idx, c in enumerate(s):
#             ed = max(ed, s.rfind(c))
#             if ed == idx:
#                 ret.append(ed-st+1)
#                 st = idx+1
#         return ret

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        st, ed = 0, 0
        ret, lst = [], defaultdict(int)
        for idx, c in enumerate(s):
            lst[c] = idx

        for idx, c in enumerate(s):
            ed = max(ed, lst[c])
            if ed == idx:
                ret.append(ed-st+1)
                st = idx+1
        return ret
