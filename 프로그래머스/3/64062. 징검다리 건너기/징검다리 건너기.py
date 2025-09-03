def solution(stones, k):

    left, right = 0, max(stones) + 1
    while left <= right:
        mid = (left + right) // 2

        current_successive = 0
        # max_successive = 0
        for stone in stones:
            if stone - mid < 0:
                current_successive += 1
                # max_successive = max(max_successive, current_successive)
            else:
                current_successive = 0
            
            if current_successive >= k:
                break
        
        if current_successive >= k:
            right = mid - 1
        else:
            left = mid + 1

    return right