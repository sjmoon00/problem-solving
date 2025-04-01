import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pok = dict()
code = dict()
for i in range(N):
    name = input().rstrip()
    pok[name] = i+1
    code[i+1] = name
for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(code[int(q)])
    else:
        print(pok[q])