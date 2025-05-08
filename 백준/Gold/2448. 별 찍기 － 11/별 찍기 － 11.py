import math
N = int(input())
itr = math.log((N // 3), 2)

base = [[' ', ' ', '*', ' ', ' ', ' '],
        [' ', '*', ' ', '*', ' ', ' '],
        ['*', '*', '*', '*', '*', ' ']]

def recur(itr):
    global base
    if itr < 0:
        return
    
    rNum, cNum = 2 * len(base), 2 * len(base[0])
    tmp = [[' '] * cNum for _ in range(rNum)]

    def draw(r, c):
        for i in range(len(base)):
            for j in range(len(base[0])):
                tmp[r + i][c + j] = base[i][j]

    draw(0, cNum // 4)
    draw(rNum // 2, 0)
    draw(rNum // 2, cNum // 2)
    
    base = [tmp[i][:] for i in range(len(tmp))]
    recur(itr - 1)

recur(itr-1)

for x in base:
    print(''.join(x))