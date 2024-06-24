class MyStack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack = []
    
    def is_empty(self):
        return len(self.stack)==0

    def is_full(self):
        return len(self.stack)==self.capacity
    
    def push(self,value):
        if len(self.stack)!= self.capacity: 
             self.stack.insert(0,value)
    
    def top(self):
        return self.stack[0]
    
    def pop(self):
        value = self.stack[0]
        del self.stack[0]
        return value
    
#test
stack1=MyStack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
