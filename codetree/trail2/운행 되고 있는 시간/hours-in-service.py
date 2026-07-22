n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

arr = [0] * 1001
for start, end in times:
    for i in range(start, end):
        arr[i] += 1

total_time = sum(1 for x in arr if x > 0)
answer = 0
for start, end in times:
    alone_time = sum(1 for x in arr[start:end] if x == 1)
    
    answer = max(answer, total_time - alone_time)

print(answer)