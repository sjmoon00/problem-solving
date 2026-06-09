from itertools import combinations
A = input()

combi = combinations(A, 2)
answer = 0
for a, b in combi:
    if a == '(' and b == ')':
        answer += 1

print(answer)