class MyQueue:
    def __init__(self, capacity):
        self.__data = []
        self.capacity = capacity

    def is_empty(self):
        if (len(self.__data) == 0):
            return True
        else:
            return False

    def is_full(self):
        if (len(self.__data) == self.capacity):
            return True
        else:
            return False

    def dequeue(self):
        return self.__data.pop(0)

    def enqueue(self, item):
        self.__data.append(item)

    def front(self):
        return self.__data[0]


queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
