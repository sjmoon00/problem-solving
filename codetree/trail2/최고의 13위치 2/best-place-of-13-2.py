n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n - 2):
        sum1 = sum(arr[i][j:j + 3])
        for k in range(i, n):
            for l in range(n - 2):
                if (i == k) and abs(l - j) < 3:
                    continue

                answer = max(answer, sum1 + sum(arr[k][l:l + 3]))

print(answer)