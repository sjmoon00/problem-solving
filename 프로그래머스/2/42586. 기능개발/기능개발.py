from collections import deque
def solution(progresses, speeds):
    answer = []
    p_q, s_q = deque(progresses), deque(speeds)
    while p_q:
        for _ in range(len(p_q)):
            p = p_q.popleft()
            s = s_q.popleft()
            p_q.append(p + s)
            s_q.append(s)
        cnt = 0
        while p_q and p_q[0] >= 100:
            cnt += 1
            p_q.popleft()
            s_q.popleft()
        if cnt != 0:
            answer.append(cnt)

    return answer