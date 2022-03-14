class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        answer = [0 for _ in range(len(T))]
        for idx, d in enumerate(T):
            while stk and T[stk[-1]] < d:
                top = stk.pop()
                answer[top] = idx-top
            stk.append(idx)
        return answer
