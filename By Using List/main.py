class stack:    #defining class stack

    def __init__(self):   # Create a empty Stack.
        self.lst = []

# method for check stack is empty...   
    def is_empty(self):
        return len(self.lst) == 0
    
# method for push element in stack....    
    def push(self,data):
        self.lst.append(data)
        return self.lst
    
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            raise IndexError("stack is Empty")
        
# method for return top element of the stack...    
    def peek(self):
        if not self.is_empty():
            return self.lst[-1]
        else:
            raise IndexError("Empty Stack")
        
# method for return size of the stack...    
    def size(self):
        return len(self.lst)



stack = stack()
if stack.is_empty():
    print("empty")
else:
    print("not empty")

stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
print("the top element is ",stack.peek())
print("Removed element is ",stack.pop())
print("the top element is ",stack.peek())
