N = int(input())
seat = list(input())

def get_distance():
    dist = 1e9
    prev = -1
    for i in range(N):
        if seat[i] == '0':
            continue
        if prev == -1:
            prev = i
        else:
            dist = min(dist, i - prev)
            prev = i
    return dist

answer = 0
for i in range(N):
    if seat[i] == '1':
        continue
    seat[i] = '1'
    for j in range(i + 1, N):
        if seat[j] == '1':
            continue
        seat[j] = '1'
        
        distance = get_distance()
        answer = max(answer, distance)

        seat[j] = '0'

    seat[i] = '0'

print(answer)