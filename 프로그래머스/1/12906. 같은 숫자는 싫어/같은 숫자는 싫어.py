def solution(arr):
    answer = []
    last = -1
    for x in arr:
        if x != last:
            answer.append(x)
            last = x
    return answer