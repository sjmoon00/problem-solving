from itertools import combinations
ability = list(map(int, input().split()))

total_idx = set(range(6))
answer = 1e9
for team1 in combinations(total_idx, 2):
    remain_idx = total_idx - set(team1)
    
    for team2 in combinations(remain_idx, 2):
        team3 = remain_idx - set(team2)

        t1, t2, t3 = sum(ability[i] for i in team1), sum(ability[i] for i in team2), sum(ability[i] for i in team3)
        best, worst = max(t1, t2, t3), min(t1, t2, t3)
        answer = min(answer, best - worst)

print(answer)