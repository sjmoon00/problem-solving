N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()

prefix = [0] * N
prefix[0] = P[0]
for i in range(1, N):
    prefix[i] = prefix[i - 1] + P[i]

answer = 0
for i in range(N):
    cost = prefix[i] - P[i] // 2
    if cost <= B:
        answer = i + 1
    else:
        break

print(answer)