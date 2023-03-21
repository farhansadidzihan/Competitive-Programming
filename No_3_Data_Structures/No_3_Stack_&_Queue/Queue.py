# || =====\\ Queue is a Linear Restricted Data Stucture //===== ||

# || Queue follows FIFO(First In Fist Out) Concept || In Queue, There are Rear and Front two pointers for Insertion & Deletion puposes ||
# || In Queue, Adding Element is called "Enqueue" & Deleting Element is called "Dequeue" ||
# || Types of Queue:- Linear Queue, Circular Queue, Priority Queue ||

# || Linear Queue ||
class Linear_Queue:
    def __init__(self):
        self.items = []
        
    def __repr__(self):
        return repr(self.items)

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.items:
            return self.items.pop(0)
        else:
            return "The Queue is Null!"
        
lq = Linear_Queue()
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.dequeue()
print(lq)

# || Circular Queue ||
class Circular_Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def __repr__(self):
        return repr(self.items)

    def enqueue(self, item):
        if self.is_full():
            print("The Queue is Full!")
            return
        else:
            print("Inserting", item)
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.max_size += 1

    def dequeue(self):
        if not self.is_empty():
            item = self.items[self.head]
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return item
        else:
            return None

    def is_empty(self):
        if not self.size:
            return True
        else:
            return False
        
    def is_full(self):
        if self.size == self.max_size:
            return True
        else:
            return False

cq = Circular_Queue(3)
cq.enqueue(100)
cq.enqueue(200)
cq.enqueue(300)
cq.dequeue()
print(cq)

# || Priority Queue ||
    # Not Created right now