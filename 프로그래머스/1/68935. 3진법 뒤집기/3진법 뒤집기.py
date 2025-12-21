def solution(n):
    answer = 0
    
    tri = ''
    while n >= 3:
        div, mod = divmod(n, 3)
        tri += str(mod)
        n = div
    tri += str(n)

    answer = int(tri, 3)
    return answer