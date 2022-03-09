class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(map(lambda x: 1 if '+' in x else -1, operations))
