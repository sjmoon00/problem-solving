n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(i, n):
        interval = arr[i:j + 1]
        avg = sum(interval) / (j - i + 1)
        if avg in interval:
            answer += 1

print(answer)