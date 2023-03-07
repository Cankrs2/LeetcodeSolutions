class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0
        result = 0
        while counter < len(s):
            if s[counter] == "I":
                result +=1
            if s[counter] == "V":
                if counter >0 and s[counter-1] == "I":
                    result +=3
                else:
                    result +=5
            if s[counter] == "X":
                if counter >0 and s[counter-1] == "I":
                    result +=8
                else:
                    result +=10
                    
            if s[counter] == "L":
                if counter >0 and s[counter-1] == "X":
                    result +=30
                else:
                    result +=50           
            if s[counter] == "C":
                if counter >0 and s[counter-1] == "X":
                    result +=80
                else:
                    result +=100
            if s[counter] == "D":
                if counter >0 and s[counter-1] == "C":
                    result +=300
                else:
                    result +=500
                    
            if s[counter] == "M":
                if counter >0 and s[counter-1] == "C":
                    result +=800
                else:
                    result +=1000
            counter +=1
        return result