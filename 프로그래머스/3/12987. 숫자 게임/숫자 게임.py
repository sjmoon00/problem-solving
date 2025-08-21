def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for a in A:
        b = B[-1]
        if b > a:
            answer += 1
            B.pop()
    return answer