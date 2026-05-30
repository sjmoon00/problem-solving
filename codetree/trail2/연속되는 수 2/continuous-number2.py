n = int(input())
arr = [int(input()) for _ in range(n)]

answer = 1
idx = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        answer = max(answer, i - idx)
        idx = i
print(answer)