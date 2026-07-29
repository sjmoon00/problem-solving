from itertools import combinations
n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

answer = 0
for i1, i2, i3 in combinations(range(n), 3):
    lines = [0] * 101
    is_overlap = False
    for i in range(n):
        if i in [i1, i2, i3]:
            continue
        
        left, right = l[i], r[i]
        for j in range(left, right + 1):
            if lines[j] > 0:
                is_overlap = True
                break
            lines[j] += 1
        
        if is_overlap:
            break
    
    if not is_overlap:
        answer += 1

print(answer)     