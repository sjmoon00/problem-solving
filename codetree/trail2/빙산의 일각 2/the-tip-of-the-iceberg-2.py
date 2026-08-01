n = int(input())
H = [int(input()) for _ in range(n)]

answer = 0
for level in range(min(H), max(H) + 1):
    arr = [x - level for x in H]

    ice = 0
    if arr[0] > 0:
        ice += 1
    for i in range(1, n):
        if arr[i] > 0 and arr[i-1] <= 0:
            ice += 1
    
    answer = max(answer, ice)

print(answer)