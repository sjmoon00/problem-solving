class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        occupied_position = [i for i, x in enumerate(flowerbed) if x == 1]
        cnt = 0

        last = -1
        term = occupied_position[0] - last - 1
        if term >= 2:
            t = term // 2
            cnt += t
        last = occupied_position[0]

        for i in occupied_position:
            term = i - last - 1
            if term <= 2:
                last = i
                continue
            t = term - 2 + 1
            cnt += t // 2

            last = i

        term = len(flowerbed) - last - 1
        if term >= 2:
            t = term // 2
            cnt += t
        
        if cnt >= n:
            return True
        else:
            return False