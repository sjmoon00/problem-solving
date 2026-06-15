from itertools import combinations
n = int(input())
arr = [int(input()) for _ in range(n)]

answer = -1
for a, b, c in combinations(arr, 3):
    candidate = a + b + c
    while a or b or c:
        aa, bb, cc = a % 10, b % 10, c % 10
        if aa + bb + cc >= 10:
            break
        a, b, c = a // 10, b // 10, c // 10
    else:
        answer = max(answer, candidate)
    
print(answer)