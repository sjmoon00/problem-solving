def solution(n, lost, reserve):
    answer = 0
    lost_s = set(lost) - set(reserve)
    reserve_s = list(set(reserve) - set(lost))
    reserve_s.sort()

    for i in reserve_s:
        left, right = i-1, i+1
        if left in lost_s:
            lost_s.remove(left)  
        elif right in lost_s:
            lost_s.remove(right)
            
    answer = n - len(lost_s)
    return answer