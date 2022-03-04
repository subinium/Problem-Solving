class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        answer = 0
        for i in range(1, l+1, 2):
            for j in range(l):
                if j+i > l:
                    break
                answer += sum(arr[j:j+i])
        return answer
