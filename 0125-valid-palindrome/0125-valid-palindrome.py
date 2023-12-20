class Solution:
    def IsAlphaNumeric(self,char):
        return (ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))
    def isPalindrome(self, s: str) -> bool:
        left,right = 0, len(s)-1
        while left < right:
            while left<right and not self.IsAlphaNumeric(s[left]):
                left +=1
            while right>left and not self.IsAlphaNumeric(s[right]):
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left,right = left+1,right-1
        return True
