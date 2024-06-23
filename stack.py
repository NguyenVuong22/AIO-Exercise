class MyStack:
    def __init__(self, capacity):
        self.__data = []
        self.capacity = capacity

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop(-1)

    def is_full(self):
        if (len(self.__data) == self.capacity):
            return True
        else:
            return False

    def top(self):
        return self.__data[len(self.__data) - 1]

    def is_empty(self):
        if (len(self.__data) == 0):
            return True
        else:
            return False


stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
