class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        left,right = 0, len(s)-1
        while left < right:
            if s[left] in vowels and s[right] not in vowels:
                right -= 1
                continue
            elif s[right] in vowels and s[left] not in vowels:
                left += 1
                continue
            elif s[left] in vowels and s[right] in vowels:
                s = s[:left] + s[right] + s[left + 1:right] + s[left] + s[right + 1:]
            
            left+=1
            right -=1
        return s