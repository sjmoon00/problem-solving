N, M = map(int, input().split())
tmp = list(map(int, input().split()))
T, true_knowes = tmp[0], set(tmp[1:])
# true_hear = set()
parties = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    n, participants = tmp[0], set(tmp[1:])
    parties.append(participants)

for _ in range(M):
    for party in parties:
        if party & true_knowes:
            true_knowes |= party
cnt = 0
for party in parties:
    if party & true_knowes:
        # 진실 말하기
        continue
    cnt += 1
print(cnt)