class CircularQue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lst = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        if self.size != 0 and self.size == self.capacity:
            return True
        return False
    
    def is_empty(self):
        if self.front == self.rear:
            return True
        
        return False
    
    def enqueue(self, x):
        if self.is_full():
            raise
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.lst[self.rear] = x
            self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise

        rtn = self.lst[self.front]
        self.lst[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return rtn
    
    def peek(self):
        if not self.is_empty():
            return self.lst[self.front]
    
    def printQue(self):
        for i in range(self.capacity):
            print(self.lst[i], end = ' ')
