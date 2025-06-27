from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(idx, x) for idx, x in enumerate(priorities)])
    
    def exist_priority_greaterthan(x):
        s = set([t[1] for t in queue])
        for i in range(x+1, 10):
            if i in s:
                return True
        return False

    while queue:
        i, x = queue.popleft()
        
        if exist_priority_greaterthan(x):
            queue.append((i, x))
            continue
        answer += 1
        if i == location:
            break
        
    return answer