from collections import defaultdict
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

arr = defaultdict(int)
for start, end in times:
    for i in range(start, end):
        arr[i] += 1

answer = 0
for start, end in times:
    t = arr.copy()
    for i in range(start, end):
        t[i] -= 1
    
    answer = max(answer, len([x for x in t.values() if x != 0]))

print(answer)