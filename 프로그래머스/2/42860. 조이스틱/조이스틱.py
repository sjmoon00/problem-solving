def solution(name):
    N = len(name)
    A, Z = ord('A'), ord('Z')
    answer = 0
    not_A = []
    for i, c in enumerate(name):
        C = ord(c)
        if c != 'A': 
            answer += min(C - A, Z - C + 1)
            not_A.append(i)
    
    if not not_A:
        return answer
    
    not_A.append(N)
    cursor_move = N-1
    for i in range(len(not_A)-1):
        left = not_A[i]
        right = N - not_A[i+1]
        if left > right:
            cursor_move = min(cursor_move, right * 2 + left)
        else:
            cursor_move = min(cursor_move, left * 2 + right)
    
    answer += cursor_move
    return answer