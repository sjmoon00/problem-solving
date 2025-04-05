def solution(n, wires):
    answer = 1e9
    G = [[] for _ in range(n+1)]
    for start, end in wires:
        G[start].append(end)
        G[end].append(start)
    
    def dfs(node, g, visited):
        if visited[node]:
            return 0
        visited[node] = True
        cnt = 1
        for n in g[node]:
            cnt += dfs(n, g, visited)
        return cnt
        
        
    for start, end in wires:
        g = [row[:] for row in G]
        g[start].remove(end)
        g[end].remove(start)

        n1 = dfs(start, g, [False]*(n+1))
        n2 = dfs(end, g, [False]*(n+1))
        answer = min(answer, abs(n1 - n2))

    return answer