#This is a stack implementation using lists

class Stack: #start of the Stack class

    def __init__(self): #initializing the stack
        self.stack = [] #starting with an empty list

    def pop(self): #popping an item out of the stack
        return self.stack.pop()

    def push(self, item): #pushing an item into the stack
        self.stack.append(item)

    def size(self): #receiving the size of the stack
        return len(self.stack)

    def show(self): #displays the full stack
        return self.stack

    def peek(self):
        if len(self.stack) == 0:
            return "The stack is empty" #if the stack is empty, then can't peek and so gives this message

        return self.stack[-1] #otherwise, we are returning the top of the stack
