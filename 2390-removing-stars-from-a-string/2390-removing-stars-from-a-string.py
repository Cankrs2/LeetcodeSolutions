class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        star_counter = 0
        for letter in s:
            stack.append(letter)
        s = ""
        while stack != []:
            letter = stack.pop()
            if letter == "*":
                star_counter += 1
                
            else:
                if star_counter == 0:
                    s = letter + s
                else:
                    star_counter -=1
        return s