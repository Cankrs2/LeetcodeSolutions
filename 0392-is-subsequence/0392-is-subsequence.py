class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        index = 0
        while index < len(t) and counter < len(s):
            if s[counter] == t[index]:
                counter += 1
            index += 1
        if counter == len(s):
            return True
        return False