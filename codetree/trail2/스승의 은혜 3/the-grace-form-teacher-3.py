N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
# P = [gift[0] for gift in gifts]
# S = [gift[1] for gift in gifts]
p_s = [sum(x) for x in gifts]
gifts = [(p_s[i], gifts[i][0], gifts[i][1]) for i in range(N)]
gifts.sort(key=lambda x: x[0])

answer = -1
for i in range(N):
    total_cost = 0
    num = 0
    for j in range(N):
        total, price, ship = gifts[j]
        if j == i:
            total_cost += (price//2 + ship)
        else:
            total_cost += total
        num += 1
        
        if total_cost <= B:
            answer = max(answer, num)
        else:
            break

print(answer)