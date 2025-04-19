import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    h_length = len(scoville)
    while scoville[0] < K:
        if h_length >= 2:
            first = hq.heappop(scoville)
            second = hq.heappop(scoville)
            if first == 0 and second == 0:
                answer = -1
                break
            mix = first + second * 2
            hq.heappush(scoville, mix)
            answer += 1
            h_length -= 1
        else:
            answer = -1
            break
    return answer