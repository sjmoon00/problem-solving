def calc_degrees(t):
    h_degree = (t % (12*60*60)) * (360 / (12*60*60))
    m_degree = (t % (60*60)) * (360 / (60*60))
    s_degree = (t % 60) * (360 / 60)
    return h_degree, m_degree, s_degree

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    begin_sec = h1*60*60 + m1*60 + s1
    end_sec = h2*60*60 + m2*60 + s2

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