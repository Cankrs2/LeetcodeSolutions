class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for char in t:
            if char not in dict:
                dict[char] = 0
            dict[char] += 1
        for i in s:
            if i in dict and dict[i] > 0:
                dict[i] -= 1
            else:
                return False
        return True
                