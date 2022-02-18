class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = dict()
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key not in keys:
                keys[key] = []
            keys[key].append(s)
        return list(keys.values())
