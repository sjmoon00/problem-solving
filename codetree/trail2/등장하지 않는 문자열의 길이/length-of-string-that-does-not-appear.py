from collections import defaultdict
N = int(input())
string = input()

d = defaultdict(int)
arr = [False] * (N + 1)
for i in range(N):
    for j in range(i, N):
        substr = string[i:j+1]
        d[substr] += 1
        if d[substr] > 1:
            arr[len(substr)] = True

for i in range(1, N + 1):
    x = arr[i]
    if not x:
        print(i)
        break