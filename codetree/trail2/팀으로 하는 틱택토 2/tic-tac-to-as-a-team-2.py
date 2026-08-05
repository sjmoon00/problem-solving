from itertools import combinations
ttt = [list(map(int, input())) for _ in range(3)]

lines = []
for i in range(3):
    row = ttt[i][:]
    col = [x[i] for x in ttt]
    lines.extend([row, col])
lines.append([ttt[0][0], ttt[1][1], ttt[2][2]])
lines.append([ttt[0][2], ttt[1][1], ttt[2][0]])

answer = 0
for a, b in combinations(range(1, 10), 2):
    for line in lines:
        if (line.count(a) == 2 and line.count(b) == 1) or (line.count(a) == 1 and line.count(b) == 2):
            answer += 1
            break

print(answer)