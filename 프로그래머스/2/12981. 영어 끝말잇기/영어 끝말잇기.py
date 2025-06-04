from collections import defaultdict
def solution(n, words):
    answer = [0, 0]
    used = set()

    cnt = 1
    def cnt_up():
        nonlocal cnt
        cnt += 1
        if cnt > n:
            cnt = 1
    
    cycle = defaultdict(int)
    last = words[0][0]
    for word in words:
        if word in used or word[0] != last:
            answer = [cnt, cycle[cnt] + 1]
            break
        
        last = word[-1]
        used.add(word)
        cycle[cnt] += 1
        cnt_up()
    return answer