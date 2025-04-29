from itertools import combinations
N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    row = list(map(int ,input().split()))
    for j, x in enumerate(row):
        if x == 1:
            houses.append((i, j))
        elif x == 2:
            chickens.append((i, j))

def calc_chicken_distance(houses, chickens):
    distance = 0
    for h in houses:
        d = 1e9
        for c in chickens:
            tmp = abs(h[0] - c[0]) + abs(h[1] - c[1])
            d = min(d, tmp)
        distance += d

    return distance

distance = 1e9
for i in range(1, M+1):
    combi = combinations(chickens, i)
    for comb in combi:
        dist = calc_chicken_distance(houses,comb)
        distance = min(distance, dist)
        
print(distance)