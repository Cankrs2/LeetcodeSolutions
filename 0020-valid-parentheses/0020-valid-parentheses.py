class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] != ")" and s[i] != "]" and s[i] != "}":
                stack.append(s[i])
            else:
                if stack != []:
                    x = stack.pop()
                    if x =="{" and s[i] != "}":
                        return False
                    if x =="[" and s[i] != "]":
                        return False
                    if x =="(" and s[i] != ")":
                        return False
                else:
                    return False
        if stack != []:
            return False
        return True