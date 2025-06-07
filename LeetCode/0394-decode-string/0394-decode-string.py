class Solution:
    def decodeString(self, s: str) -> str:
        answer = ''
        stack = []
        num = 0
        for x in s:
            if x.isdigit():
               num = num * 10 + int(x)
            elif x == '[':
                stack.append((num, answer))
                num = 0
                answer = ''
            elif x == ']':
                n, string = stack.pop()
                answer = string + n * answer
            else:
                answer += x
    
        return answer