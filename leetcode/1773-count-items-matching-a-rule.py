class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleIdx = ['type', 'color', 'name'].index(ruleKey)
        return len(list(filter(lambda x: x[ruleIdx] == ruleValue, items)))
