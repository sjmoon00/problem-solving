n = int(input())
arr = list(map(int, input().split()))

answer = 0
for k in range(min(arr), max(arr) + 1):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            ai, aj = arr[i], arr[j]
            if (aj - k) == (k - ai):
                cnt += 1
    answer = max(answer, cnt)

print(answer)