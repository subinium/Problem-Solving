class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk, idx = [], 0
        for val in pushed:
            stk.append(val)
            while stk and stk[-1] == popped[idx]:
                stk.pop()
                idx += 1

        return len(stk) == 0
