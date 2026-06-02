N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

arr = [0] * (N + 1)
for s in student:
    arr[s] += 1
    if arr[s] >= K:
        print(s)
        break