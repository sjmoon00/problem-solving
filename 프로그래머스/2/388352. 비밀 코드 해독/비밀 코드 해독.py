from itertools import combinations
def solution(n, q, ans):
    answer = 0
    comb = combinations(range(1, n+1), 5)
    for com in comb:
        t = 0
        for question, result in zip(q, ans):
            if len(set(com) & set(question)) == result:
                t += 1
        if t == len(q):
            answer += 1
    
    return answer