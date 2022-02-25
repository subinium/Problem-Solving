class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        l1, l2 = len(version1), len(version2)
        if l1 < l2:
            version1 += [0 for _ in range(l2-l1)]
        elif l1 > l2:
            version2 += [0 for _ in range(l1-l2)]

        if version1 == version2:
            return 0
        elif version1 < version2:
            return -1
        else:
            return 1
