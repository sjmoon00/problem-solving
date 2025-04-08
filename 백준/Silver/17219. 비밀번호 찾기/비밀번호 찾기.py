import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = {}
for _ in range(N):
    address, pwd = input().rstrip().split()
    d[address] = pwd
for _ in range(M):
    print(d[input().rstrip()])