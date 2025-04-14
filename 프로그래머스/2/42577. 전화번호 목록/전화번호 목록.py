def solution(phone_book):
    answer = True
    s = set()
    for phone in phone_book:
        tmp = []
        for p in phone[:-1]:
            tmp.append(p)
            s.add(''.join(tmp))
    for phone in phone_book:
        if phone in s:
                answer = False
                break 
    return answer