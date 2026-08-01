n = int(input())
H = [int(input()) for _ in range(n)]

answer = 0
for level in range(min(H), max(H) + 1):
    arr = [x - level for x in H]
    start, end = 0, 0
    for i in range(n):
        if arr[i] > 0:
            start = i
            break
    for i in range(n - 1, -1, -1):
        if arr[i] > 0:
            end = i
            break

    zero = 0
    for i in range(start, end + 1):
        if arr[i] <= 0 and arr[i-1 if i-1 >= 0 else 0] > 0:
            zero += 1
    
    answer = max(answer, zero + 1)

print(answer)