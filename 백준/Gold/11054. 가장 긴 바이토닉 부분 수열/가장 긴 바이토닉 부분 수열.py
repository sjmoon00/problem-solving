N = int(input())
A = list(map(int, input().split()))

dp_inc = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

dp_dsc = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j]:
            dp_dsc[i] = max(dp_dsc[i], dp_dsc[j] + 1)

answer = [0] * N
for i in range(N):
    answer[i] = dp_inc[i] + dp_dsc[i] - 1

print(max(answer))