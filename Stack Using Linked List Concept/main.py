class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self,):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start is None
    
    def push(self,data):
        n = Node(data, self.start)
        self.start = n
        self.item_count+=1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack 'out of index'!")
        elif self.start.next is None:
            self.start = None
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("stack 'out of elements'!")

    def size(self):
        return self.item_count
                



stack = Stack()
stack.push(5)
stack.push(7)
stack.push(8)
stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
print("size is ",stack.size())
print("top element = " ,stack.peek())
