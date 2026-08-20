from itertools import permutations
n = int(input())
adjacent = list(map(int, input().split())) if n >= 2 else []

def main():
    if n == 1:
        print(adjacent)
        return
    
    for arr in permutations(range(1, n+1), n):
        adj = [arr[i]+arr[i+1] for i in range(n-1)]
        if adj == adjacent:
            print(*arr)
            return

main()