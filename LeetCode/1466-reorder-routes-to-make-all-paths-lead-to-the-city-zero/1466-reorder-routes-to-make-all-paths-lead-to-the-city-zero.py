from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        tree = defaultdict(set) 
        for parent, child in connections:
            tree[parent].add((child, True))
            tree[child].add((parent, False))
        
        cnt = 0
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        
        while queue:
            node = queue.popleft()
            for next_node, is_connected in tree[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                queue.append(next_node)
                if is_connected:
                    cnt += 1 
        
        return cnt