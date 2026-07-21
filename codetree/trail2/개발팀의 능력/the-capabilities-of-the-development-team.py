from itertools import combinations
arr = list(map(int, input().split()))

answer = -1
idx_pool = set(range(5))
for team1 in combinations(idx_pool, 2):
    remain_pool = idx_pool - set(team1)
    for team2 in combinations(remain_pool, 2):
        team3 = remain_pool - set(team2)
        t1, t2, t3 = sum(arr[i] for i in team1), sum(arr[i] for i in team2), sum(arr[i] for i in team3)
        if t1 == t2 or t2 == t3 or t1 == t3:
            continue
        
        best, worst = max(t1, t2, t3), min(t1, t2, t3)
        if answer == -1:
            answer = best - worst
        else:
            answer = min(answer, best - worst)

print(answer)