class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        s+= "+"
        curr = 0
        operation = "+"
        for char in s:
            if char.isdigit():
                curr = 10*curr + int(char)
            elif char == " ": continue
            else:
                if operation == "+":
                    stack.append(curr)
                elif operation == "-":
                    stack.append(-curr)
                elif operation =="*":
                    num = stack.pop()
                    stack.append(num*curr)
                elif operation == "/":
                    num = stack.pop()
                    if num <0: 
                        num*=-1
                        stack.append(-1*(num//curr))
                    else:
                        stack.append(num//curr)
                    
                curr = 0
                operation = char
        return sum(stack)