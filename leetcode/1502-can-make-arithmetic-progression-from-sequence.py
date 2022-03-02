class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = []
        for i in range(len(arr)-1):
            diff.append(arr[i+1]-arr[i])
        return len(set(diff)) == 1
