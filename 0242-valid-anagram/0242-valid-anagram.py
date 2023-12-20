class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dict.append(s[i])
        for j in range(len(t)):
            if t[j] in dict:
                dict.remove(t[j])
            else:
                return False
        return True