def solution(numbers:list):
    N = len(numbers)
    answer = [-1] * N
    stack = []

    for i in range(N):
        while stack and numbers[i] > numbers[stack[-1]]:
            prev_greater_idx = stack.pop()
            answer[prev_greater_idx] = numbers[i]
        stack.append(i)
    
    return answer