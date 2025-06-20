class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        diff = (len(v1) - len(v2))
        if diff < 0:
            for _ in range(-diff):
                v1.append(0)
        elif diff > 0:
            for _ in range(diff):
                v2.append(0)
        
        for x, y in zip(v1, v2):
            if x < y:
                return -1
            elif x > y:
                return 1
        else:
            return 0