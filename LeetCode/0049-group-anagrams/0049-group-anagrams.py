from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            c = tuple(sorted(Counter(s).items()))
            dic[c].append(s)
        return list(dic.values())