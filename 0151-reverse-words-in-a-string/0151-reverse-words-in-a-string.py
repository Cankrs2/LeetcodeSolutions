class Solution:
    def reverseWords(self, s: str) -> str:
        is_space = 0
        res = ""
        word = ""
        counter = -1
        while counter*-1 <= len(s):
            if len(word) != 0 and s[counter] == " " and is_space != 1:
                is_space = 1
                res += word
                word = ""
            elif s[counter] != " ":
                if is_space == 1:
                    res += " "
                    is_space = 0
                word = s[counter] + word
            counter -= 1
        res+=word   
        return res