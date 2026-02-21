def solution(h1, m1, s1, h2, m2, s2):
    H, M, S = 12*60*60, 60*60, 60
    answer = 0
    begin_sec = h1*60*60 + m1*60 + s1
    end_sec = h2*60*60 + m2*60 + s2

    def calc_degrees(t):
        h_degree = (t % H) * (360 / H)
        m_degree = (t % M) * (360 / M)
        s_degree = (t % S) * (360 / S)
        return h_degree, m_degree, s_degree

    h1, m1, s1 = calc_degrees(begin_sec)
    if s1 == h1 or s1 == m1:
        answer += 1

    for t in range(begin_sec, end_sec):
        h1, m1, s1 = calc_degrees(t)
        h2, m2, s2 = calc_degrees(t+1)

        h2 = 360 if h2 == 0 else h2
        m2 = 360 if m2 == 0 else m2
        s2 = 360 if s2 == 0 else s2

        if s1 < h1 and s2 >= h2:
            answer += 1
        if s1 < m1 and s2 >= m2:
            answer += 1
        if s2 == h2 == m2:
            answer -= 1

    return answer