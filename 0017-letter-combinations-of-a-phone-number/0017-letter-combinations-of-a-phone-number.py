class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w', 'x', 'y','z']
        }
        
        result = set()
        
        def backtrack(index,choosen):
            if index >= len(digits):
                if(choosen):
                    result.add(choosen)
                return
            for i in phone[digits[index]]:
                backtrack(index+1,choosen+i)
            
        backtrack(0,"")
        
        return result