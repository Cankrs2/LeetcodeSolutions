class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        res = ""
        while counter < len(word1) and counter < len(word2):
            res += word1[counter]
            res += word2[counter]
            counter +=1
        while counter < len(word1):
            res += word1[counter]
            counter +=1
        while counter < len(word2):
            res += word2[counter]
            counter +=1
        return res