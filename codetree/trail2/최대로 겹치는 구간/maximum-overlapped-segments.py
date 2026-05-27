n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100
arr = [0] * 201
for segment in segments:
    a, b = segment[0] + offset, segment[1] + offset
    for i in range(a, b):
        arr[i] += 1

print(max(arr))