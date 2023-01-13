class Solution:
    def countDigits(self,num: int) -> int:
        counter = 0
        strnum = str(num)
        for digit in strnum:
            if num%int(digit) == 0:
                counter +=1
        return counter