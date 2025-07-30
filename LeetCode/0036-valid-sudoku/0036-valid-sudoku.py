class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_subBox(x, y):
            subBox = [t[y:y+3] for t in board[x:x+3]]
            s = set()
            cnt = 0
            for row in subBox:
                for t in row:
                    if t != '.':
                        s.add(t)
                        cnt += 1
            if len(s) != cnt:
                return False
            return True
        def check_row(x, y):
            row = board[x]
            s = set()
            cnt = 0
            for t in row:
                if t != '.':
                    s.add(t)
                    cnt += 1
            if len(s) != cnt:
                return False
            return True
        def check_col(x, y):
            col = [t[y] for t in board]
            s = set()
            cnt = 0
            for t in col:
                if t != '.':
                    s.add(t)
                    cnt += 1
            if len(s) != cnt:
                return False
            return True
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_subBox(i, j):
                    return False
        
        for i in range(9):
            if not check_row(i, 0):
                return False
            if not check_col(0, i):
                return False
        
        return True