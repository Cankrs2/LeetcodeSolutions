class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        
        while counter < len(flowerbed) and n != 0:
            if flowerbed[counter] == 1:
                counter +=2
                continue
            elif counter < len(flowerbed) -1 and flowerbed[counter+1] == 1:
                counter +=3
            else:
                flowerbed[counter] = 1
                n -= 1
        if n == 0: return True
        return False