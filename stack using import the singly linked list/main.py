from linkedlist import *    # importing linked list class

# make a stack class and initialise linked list object....
class Stack:
    def __init__(self):
        self.stack = SLL()
        self.item_count = 0

# function for chacking empty 
    def is_empty(self):
        return self.stack.is_empty
    
# function for push the element in stack by using linked list insert at start option...
    def push(self,data):
        self.stack.insert_at_start(data)
        self.item_count+=1
    
# function for pop the element from stack by using linked list delete at start option...
    def pop(self):
        if self.stack.is_empty():
            raise IndexError("'out of elements'")
        else:
            data = self.stack.start.item
            self.stack.delete_first()
            self.item_count-=1
            return data
        
# return the  top element of stack
    def peek(self):
        return self.stack.start.item

# return the count variable to check the length
    def size(self):
        return self.item_count


stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)

print("pop element is ",stack.pop())
print("top element is ",stack.peek())
print("length of stack is ",stack.size())
