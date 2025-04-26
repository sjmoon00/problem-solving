def solution(numbers, target):
    answer = 0
    N = len(numbers)
    def dfs(total, i):
        nonlocal answer
        if i == N:
            if total == target:
                answer += 1
            return
        
        dfs(total + numbers[i], i + 1)
        dfs(total - numbers[i], i + 1)
    
    dfs(0, 0)
    return answer