from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        queue = deque([(entrance[0], entrance[1], 0)])
        N, M = len(maze), len(maze[0]) 
        visited = [[False] * M for _ in range(N)]
        visited[entrance[0]][entrance[1]] = True
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        answer = 1e9
        while queue:
            x, y, cnt = queue.popleft()

            for d in dirs:
                nx, ny = x + d[0], y + d[1]

                if not(0 <= nx < N) or not(0 <= ny < M):
                    if [x, y] == entrance:
                        continue
                    answer = min(answer, cnt)
                    continue
                if visited[nx][ny] or maze[nx][ny] == '+':
                    continue
                
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
            
        return answer if answer != 1e9 else -1