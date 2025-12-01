import math
def solution(m, n, startX, startY, balls):
    answer = []

    def calc_distance_square(ball):
        dists = []
        bx, by = ball
        up, down= (n - startY) + abs(bx - startX) + (n - by), (startY) + abs(bx - startX) + (by)
        left, right = startX + abs(by - startY) + bx, (m - startX) + abs(by - startY) + (m - bx)

        # d = min([up, down, left, right])
        
        if not((startX == bx) and (by > startY)):
            h1, h2 = n - startY, n - by
            w = abs(bx - startX)
            w1 = w * h1 / (h1 + h2)
            
            dist1 = math.sqrt(h1 ** 2 + w1 ** 2)
            dist = (h1 + h2) / h1 * dist1
            dists.append(round(dist ** 2))
                
        if not((startX == bx) and (by < startY)):
            h1, h2 = startY, by
            w = abs(bx - startX)
            w1 = w * h1 / (h1 + h2)
            
            dist1 = math.sqrt(h1 ** 2 + w1 ** 2)
            dist = (h1 + h2) / h1 * dist1
            dists.append(round(dist ** 2))

        if not((startY == by) and (bx < startX)):
            w1, w2 = startX, bx
            h = abs(by - startY)
            h1 = h * w1 / (w1 + w2)

            dist1 = math.sqrt(h1 ** 2 + w1 ** 2)
            dist = (w1 + w2) / w1 * dist1
            dists.append(round(dist ** 2))

        if not((startY == by) and (bx > startX)):
            w1, w2 = m - startX, m - bx
            h = abs(by - startY)
            h1 = h * w1 / (w1 + w2)

            dist1 = math.sqrt(h1 ** 2 + w1 ** 2)
            dist = (w1 + w2) / w1 * dist1
            dists.append(round(dist ** 2))

        answer.append(min(dists))

    for ball in balls:
        calc_distance_square(ball)
    
    return answer