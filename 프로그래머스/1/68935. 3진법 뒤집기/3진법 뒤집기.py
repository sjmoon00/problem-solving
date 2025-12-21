def solution(n):
    answer = 0
    
    tri = ''
    while n:
        div, mod = divmod(n, 3)
        tri += str(mod)
        n = div

    answer = int(tri, 3)
    return answer