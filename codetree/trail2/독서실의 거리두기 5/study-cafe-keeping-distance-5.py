N = int(input())
seat = list(input())

answer = 0
empty = []
for i in range(N):
    if seat[i] == '0':
        empty.append(i)

for e_idx in empty:
    seat[e_idx] = '1'
    prev_s = -1
    distance = 1e9
    for i, s in enumerate(seat):
        if s == '1':
            if prev_s == -1:
                prev_s = i
            else:
                distance = min(distance, i - prev_s)
                prev_s = i
    answer = max(answer, distance)
    seat[e_idx] = '0'

print(answer)