class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack2 == []:
            self.copy_stack(self.stack,self.stack2)
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2 == []:
            self.copy_stack(self.stack,self.stack2)
        x = self.stack2.pop()
        self.stack2.append(x)
        return x

    def empty(self) -> bool:
        if self.stack == [] and self.stack2 == []:
            return True
        return False
    
    def copy_stack(self,stack,stack2):
        while stack !=[]:
            stack2.append(stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()