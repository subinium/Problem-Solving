class Solution:
    def decodeString(self, s: str) -> str:
        stk, val, ret = [], "", ""
        for idx, c in enumerate(s):
            if c=='[': stk.append(idx)
            elif c==']': top = stk.pop()
            if stk: continue
            if c==']':
                ret += int(val)*self.decodeString(s[top+1:idx])
                val = ""
            elif c.isnumeric(): val+=c
            else: ret+=c
        return ret