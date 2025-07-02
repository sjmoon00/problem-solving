def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    elif N == 2:
        print(1)
        return
    
    buildings = []
    bb = map(int, input().split())
    for i, b in enumerate(bb):
        buildings.append((i, b))

    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue

            x1, y1, x2, y2 = buildings[i][0], buildings[i][1], buildings[j][0], buildings[j][1]
            if x1 > x2:
                t = x1
                x1 = x2
                x2 = t
                t = y1
                y1 = y2
                y2 = t
            a = (y2 - y1) / (x2 - x1)
            for k in range(x1+1, x2):
                x, height = buildings[k][0], buildings[k][1]
                line = a * (x - x1) + y1
                if height >= line:
                    break
            else:
                cnt += 1
        answer = max(answer, cnt)
    
    print(answer)

main()