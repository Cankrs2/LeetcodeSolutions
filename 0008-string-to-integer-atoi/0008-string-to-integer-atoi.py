class Solution:
    def myAtoi(self, s: str) -> int:
        nums = ["1","2","3","4","5","6","7","8","9"]
        i = 0
        sign = 1
        result = ""
        if s == "": return 0
        while i<len(s) and s[i] == " ":
            i+=1
        if i >= len(s): return 0
        if s[i] == "-" or s[i] == "+": 
            if s[i] == "-":
                sign = -1
            i+=1
        while i<len(s):
            if s[i] in nums:
                result = result + s[i]
            elif s[i] == "0":
                if result == "":
                    i+=1 
                    continue
                result = result + s[i]
            else:
                break
            i+=1
        if result == "":
            return 0
        result = self.is_integer(sign*int(result))
        return result
        
    def is_integer(self,result):
        if result > pow(2, 31) -1:
            return pow(2, 31) -1
        if result < -1*pow(2, 31):
            return -1*pow(2, 31)
        return result