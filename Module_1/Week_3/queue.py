class MyQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[]
        
    
    def is_empty(self):
        return len(self.queue)==0
    
    def is_full(self):
        return len(self.queue)== self.capacity
    
    def dequeue(self):
        value=self.queue[len(self.queue)-1]
        del self.queue[len(self.queue)-1]
        return value
    
    def enqueue(self,value):
        self.queue.insert(0,value)
    
    def front(self):
        return self.queue[len(self.queue)-1]
    

#test
queue1=MyQueue(5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
