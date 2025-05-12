# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bottom, top = 1, n
        while True:
            num = (bottom + top) // 2
            result = guess(num)
            if result == -1:
                top = num - 1
            elif result == 1:
                bottom = num + 1
            else:
                return num