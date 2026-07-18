from itertools import permutations
ability = list(map(int, input().split()))

answer = 1e9
for teams in permutations(ability):
    t1, t2, t3 = sum(teams[:2]), sum(teams[2: 4]), sum(teams[4: 6])
    best, worst = max(t1, t2, t3), min(t1, t2, t3)
    answer = min(answer, best - worst)

print(answer)