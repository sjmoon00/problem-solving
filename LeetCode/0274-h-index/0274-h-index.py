class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        h_idx = 0
        for h in range(N, -1, -1):
            t = [x for x in citations if x >= h]
            if len(t) >= h:
                h_idx = h
                break

        return h_idx