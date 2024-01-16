
# making a stack by extanding list class
class Stack(list): #extend the list class.. 
            
    def is_empty(self):
        return self == 0
    
    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
# use super keyword coz of overriding if we could self.pop() then it run for the both class list and stack so its genrate recursion thats why we use super() key it only run the function in stack class
           return super().pop()  
        else:
            raise IndexError("Stack-out of Index!")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Empty Stack!!")
        
    def size(self):
        return len(self)
    
# override the insert function coz we don't want to permit insert capability in our stack   
    def insert(self,index,data):
        raise AttributeError("no attribute 'insert' in Stack!")
    
list = Stack()
list.push(10)
list.push(20)
list.push(30)
print("top value = ",list.peek())
print("size is ",list.size())
