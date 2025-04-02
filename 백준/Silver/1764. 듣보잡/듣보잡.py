import sys
input = sys.stdin.readline
N, M = map(int, input().split())
not_heared = set()
not_seen = set()
for _ in range(N):
    name = input().rstrip()
    not_heared.add(name)
for _ in range(M):
    name = input().rstrip()
    not_seen.add(name)

not_heared_not_seen = not_heared.intersection(not_seen)
print(len(not_heared_not_seen))
for n in sorted(not_heared_not_seen):
    print(n)