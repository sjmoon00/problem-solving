from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntr = Counter(arr)
        s = set()
        for value in cntr.values():
            if value in s:
                return False
            s.add(value)
        return True