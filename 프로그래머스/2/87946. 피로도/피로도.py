from itertools import permutations
def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    perms = permutations(dungeons, N)
    
    for perm in perms:
        my_k = k
        cnt = 0
        for require, consume in perm:
            if my_k < require:
                continue
            
            my_k -= consume
            cnt += 1
        answer = max(answer, cnt)
    
    return answer