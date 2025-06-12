from collections import defaultdict
exp = input()
answer = ''
stack = []
priority = defaultdict(int)
priority.update({'+': 1, '-' : 1, '*' : 2, '/' : 2})

for x in exp:
    if x.isalpha():
        answer += x
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    elif x == '+' or x == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(x)
    elif x == '*' or x == '/':
        while stack and priority[stack[-1]] == 2:
            answer += stack.pop()
        stack.append(x)
while stack:
    answer += stack.pop()
print(answer)