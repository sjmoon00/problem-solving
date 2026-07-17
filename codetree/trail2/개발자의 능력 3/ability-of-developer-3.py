from itertools import combinations
abilities = list(map(int, input().split()))

answer = 1e9
total = sum(abilities)
for picks in combinations(abilities, 3):
    another = total - sum(picks)
    answer = min(answer, abs(sum(picks) - another))

print(answer)