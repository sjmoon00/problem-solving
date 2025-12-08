import heapq as hq
def solution(n, k, enemy):
    answer = 0
    heap = []
    for i, e in enumerate(enemy):
        n -= e
        hq.heappush(heap, -e)

        if n < 0:
            while k > 0 and n < 0:
                k -= 1
                ee = -hq.heappop(heap)
                n += ee

        if n < 0:
            break
        answer = i + 1

    return answer