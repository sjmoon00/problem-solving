N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

def main():
    x, y = 0, 0
    d = {'E': (1, 0), 'W': (-1, 0), 'S': (0, -1), 'N': (0, 1)}
    time = 0
    for direction, distance in zip(dir, dist):
        for _ in range(distance):
            x += d[direction][0]
            y += d[direction][1]
            time += 1
            if (x, y) == (0, 0):
                print(time)
                return
    print(-1)
main()