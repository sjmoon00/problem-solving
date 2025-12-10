def solution(word):
    answer = 0
    word += '_' * (5 - len(word))
    word = list(word)
    d = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    pos = {0: 1, 1: 6, 2: 31, 3: 156, 4: 781}
    
    cur = 0
    while word:
        w = word.pop()

        if w == '_':
            cur += 1
        else:
            position = pos[cur]
            num = d[w]
            answer += 1 + position * num
            cur += 1

    return answer