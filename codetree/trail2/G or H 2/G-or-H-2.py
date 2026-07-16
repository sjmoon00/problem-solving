from collections import defaultdict
n = int(input())
people = [list(input().split()) for _ in range(n)]
# pos = [int(p[0]) for p in people]
# alpha = [p[1] for p in people]
people = [[int(x[0]), x[1]] for x in people]

people.sort(key= lambda x: x[0])
answer = 0
for start in range(n):
    for end in range(start, n):
        d = defaultdict(int)
        for i in range(start, end + 1):
            pos, alpha = people[i][0], people[i][1]
            d[alpha] += 1
        
        if d['G'] == d['H'] or d['G'] == 0 or d['H'] == 0:
            s_idx, e_idx = people[start][0], people[end][0]
            answer = max(answer, e_idx - s_idx)

print(answer)