from collections import Counter
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

arr = [('', 0, 0)] * 200001
idx = 100000
for distance, direction in zip(x, dir):
    for i in range(distance):
        tile, white, black = arr[idx]
        if direction == 'R':
            nblack = black + 1
            if tile == 'G' or (white >= 2 and nblack >= 2):
                arr[idx] = ('G', white, nblack)
            else:
                arr[idx] = ('B', white, nblack)

            if i < distance - 1:    
                idx += 1
        else:
            nwhite = white + 1
            if tile == 'G' or (nwhite >= 2 and black >= 2):
                arr[idx] = ('G', nwhite, black)
            else:
                arr[idx] = ('W', nwhite, black)

            if i < distance - 1:
                idx -= 1

c = Counter(x[0] for x in arr)
print(c['W'], c['B'], c['G'])