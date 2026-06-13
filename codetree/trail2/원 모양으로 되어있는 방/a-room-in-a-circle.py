n = int(input())
a = [int(input()) for _ in range(n)]

answer = 1e9
people = sum(a)
for start_idx in range(n):

    curr_idx = start_idx
    p = people
    cnt = 0
    for _ in range(n):
        p -= a[curr_idx]
        cnt += p
        curr_idx = (curr_idx + 1) % n
    
    answer = min(answer, cnt)

print(answer)