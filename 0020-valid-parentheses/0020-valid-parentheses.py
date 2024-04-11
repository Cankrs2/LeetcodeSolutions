class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        
        for i in s:
            if i == "(" or i == "[" or i == "{":
                opens.append(i)
            else:
                if len(opens) != 0:
                    a = opens.pop()
                    if a == "(" and i != ")" or a == "[" and i != "]" or a == "{" and i != "}":
                        return False
                else: 
                    return False
        if len(opens) != 0:
            return False
        
        return True
