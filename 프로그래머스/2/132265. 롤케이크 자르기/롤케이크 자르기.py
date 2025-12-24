from collections import Counter
def solution(topping):
    answer = 0
    N = len(topping)
    left, right = Counter([]), Counter(topping)

    for i in range(N):
        x = topping[i]
        left[x] += 1
        right[x] -= 1

        if right[x] == 0:
            right.pop(x)

        if len(left.values()) == len(right.values()):
            answer += 1
        
    return answer