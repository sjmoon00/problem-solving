def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    used = [False] * N

    def permutation(result, used):
        nonlocal answer
        if len(result) == N:
            cnt = calc(result)
            answer = max(answer, cnt)

        for i in range(N):
            if used[i]:
                continue
            result.append(dungeons[i])
            used[i] = True
            permutation(result, used)
            used[i] = False
            result.pop()

    def calc(result):
        my_k = k
        cnt = 0
        for require, consume in result:
            if my_k < require:
                continue
            
            my_k -= consume
            cnt += 1
        return cnt
    
    permutation([], used)
    return answer