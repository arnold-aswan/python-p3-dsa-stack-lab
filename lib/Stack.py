class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        
    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            item = self.items[-1]
            self.items.pop()
            return item

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        items = self.items[::-1]
        
        for i in range(len(items)):
            if items[i] == target:
                return i 
        return -1
        
            