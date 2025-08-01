from collections import defaultdict, deque
N, K = map(int, input().split())
MAX_SIZE = 100001
visited = defaultdict(lambda : -1)
visited[N] = 0

queue = deque([N])
cnt = 0
while queue:
    idx = queue.popleft()

    if idx == K:
        cnt += 1
    
    for n_idx in [idx - 1, idx + 1, 2 * idx]:
        if not(0 <= n_idx < MAX_SIZE):
            continue
        
        if visited[n_idx] == -1 or visited[n_idx] >= visited[idx] + 1:
            visited[n_idx] = visited[idx] + 1
            queue.append(n_idx)

print(visited[K])
print(cnt)