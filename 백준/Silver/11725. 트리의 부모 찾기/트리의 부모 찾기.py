from collections import defaultdict, deque
N = int(input())
tree = defaultdict(list)
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

answer = [0] * (N+1)
queue = deque([1])
visited = [False] * (N+1)
visited[1] = True
while queue:
    parent = queue.popleft()
    children = tree[parent]
    for child in children:
        if visited[child]:
            continue
        answer[child] = parent
        visited[child] = True
        queue.append(child)

for i in range(2, N+1):
    print(answer[i])