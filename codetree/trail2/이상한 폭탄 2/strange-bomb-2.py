N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

answer = -1
for i in range(N):
    bomb1 = num[i]
    for j in range(i + 1, min(i+K+1, N)):
        bomb2 = num[j]
        if bomb1 == bomb2:
            answer = max(answer, bomb1)

print(answer)