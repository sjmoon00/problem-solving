class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        answer = []
        candid = []
        N = len(digits)
        for d in digits:
            candid.append(keypad[d])
        
        def dfs(n, combi):
            if n == N:
                if N != 0:
                    answer.append(combi)
                return
            
            for x in candid[n]:
                dfs(n + 1, combi + x)

        dfs(0, '')
        return answer