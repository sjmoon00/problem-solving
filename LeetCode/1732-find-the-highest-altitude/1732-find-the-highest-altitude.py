class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer, t = 0, 0
        for g in gain:
            t += g
            answer = max(answer, t)
        return answer