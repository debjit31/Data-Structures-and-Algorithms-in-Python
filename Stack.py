import time
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) <= 0:
            print("Underflow!!!")
        else:
            print(self.stack.pop())

    def peek(self):
        print(self.stack[-1]) 

    def display(self):
        print(self.stack)
    
stk = Stack()
stk.push(5)
stk.push(-1)
stk.push(4)
stk.push(3)
stk.display()
stk.pop()
stk.pop()
stk.peek()
stk.display()
print(time.strftime("%d/%m/%Y"))
