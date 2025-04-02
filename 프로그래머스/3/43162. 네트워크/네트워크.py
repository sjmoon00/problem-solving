def dfs(n, computers, i, visited):
    stack = []
    stack.append(i)
    while stack:
        node = stack.pop()
        neighbors = computers[node]
        for idx, nei in enumerate(neighbors):
            if nei == 1:
                if visited[idx]:
                    continue
                visited[idx] = True
                stack.append(idx)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1

    return answer