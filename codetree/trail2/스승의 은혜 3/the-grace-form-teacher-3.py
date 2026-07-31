N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
p_s = [sum(x) for x in gifts]
gifts = [(p_s[i], gifts[i][0], gifts[i][1]) for i in range(N)]
gifts.sort(key=lambda x: x[0])

answer = 0
for i in range(N):
    total, price, ship = gifts[i]
    cost_i = price // 2 + ship
    if cost_i > B:
        continue
    
    total_cost = cost_i
    num = 1
    for j in range(N):
        if j == i:
            continue
        
        if total_cost + gifts[j][0] <= B:
            total_cost += gifts[j][0]
            num += 1
        else:
            break
    answer = max(answer, num)

print(answer)