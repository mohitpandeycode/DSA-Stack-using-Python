from SLL import *  # importing singly linked list...

# create stack class...
class Stack(SLL):

#creating item count to get size of stack and call super class init method...
    def __init__(self):
        super().__init__()
        self.item_count = 0  

# creating func. for check stack is empty or not...  
    def is_empty(self):
        return super().is_empty()
    
# creating func. for push data in stack...  
    def push(self,data):
        self.insert_at_start(data)
        self.item_count += 1

# creating func. for delete the data from stack....
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            data = self.start.item
            self.delete_first()
            self.item_count -= 1
            return data
        
# creating func for return the top element of the stack...
    def peek(self):
        return self.start.item
    
# return the size of the stack    
    def size(self):
        return self.item_count
    
# handling these functions errors by overriding...

    def delete_last(self):
        raise ModuleNotFoundError("Function not exist")
    def delete_item(self, data):
        raise ModuleNotFoundError("Function not exist")
    def insert_after(self, temp, data):
        raise ModuleNotFoundError("Function not exist")
    def insert_at_last(self, data):
        raise ModuleNotFoundError("Function not exist")
    def print_list(self):
        raise ModuleNotFoundError("Function not exist")



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("top element is ",stack.peek())
print("Size of Stack is ",stack.size())
print("remove element is ",stack.pop())
print("Now the top element is ",stack.peek())
print("Now Size of Stack is ",stack.size())
stack.delete_last()
