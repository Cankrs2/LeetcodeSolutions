class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = -1
        curr_vowel = 0
        vowels = "aeiou"
        for i in range(k):
            if s[i] in vowels:
                curr_vowel+=1
        max_vowel = max(max_vowel,curr_vowel)
        for j in range(k,len(s)):
            if s[j-k] in vowels: curr_vowel-=1
            if s[j] in vowels: curr_vowel += 1
            max_vowel = max(max_vowel,curr_vowel)
        return max_vowel