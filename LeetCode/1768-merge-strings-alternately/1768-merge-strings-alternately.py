class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        if len(word1) > len(word2):
            for i in range(len(word2)):
                result.append(word1[i])
                result.append(word2[i])
            result.extend(word1[len(word2):])
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                result.append(word1[i])
                result.append(word2[i])
            result.extend(word2[len(word1):])
        else:
            for i in range(len(word1)):
                result.append(word1[i])
                result.append(word2[i])
        return ''.join(result)