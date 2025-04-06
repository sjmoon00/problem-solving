def solution(n, info):
    max_diff = 0
    best_shot = [-1]

    def dfs(idx, arrow_left, ryan_history):
        nonlocal max_diff, best_shot

        if idx == 11 or arrow_left == 0:
            ryan_score, apeach_score = 0, 0
            for i in range(11):
                if info[i] >= ryan_history[i]:
                    if info[i] > 0:
                        apeach_score += 10-i
                else:
                    ryan_score += 10-i
            diff = ryan_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                best_shot = ryan_history[:]
                best_shot[-1] += arrow_left
            elif diff == max_diff and diff > 0:
                for i in range(10, -1, -1):
                    if ryan_history[i] > best_shot[i]:
                        best_shot = ryan_history[:]
                        best_shot[-1] += arrow_left
                        break
                    elif ryan_history[i] < best_shot[i]:
                        break
            return
        
        need = info[idx] + 1
        if arrow_left >= need:
            ryan_history[idx] = need
            dfs(idx + 1, arrow_left - need, ryan_history)
            ryan_history[idx] = 0

        dfs(idx + 1, arrow_left, ryan_history)
    
    dfs(0, n, [0] * 11)
    return best_shot if max_diff > 0 else [-1]