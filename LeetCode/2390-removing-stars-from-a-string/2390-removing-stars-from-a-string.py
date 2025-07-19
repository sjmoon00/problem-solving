class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for x in s:
            if x != '*':
                answer.append(x)
            else:
                answer.pop()
        return ''.join(answer)