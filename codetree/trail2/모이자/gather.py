n = int(input())
A = list(map(int, input().split()))

arr = [0] * n
for i, a in enumerate(A):
    for j in range(n):
        arr[j] += a * abs(i - j)

print(min(arr))