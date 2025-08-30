# Method - 1 (Top of primary stack is equivalent to front of the queue):


# Implemented yesterday (Day46.)


# Method - 2 (Top of primary stack is equivalent to rear of the queue):
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return temp

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        temp = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return temp

    def empty(self) -> bool:
        return (not self.s1) and not (self.s2)


# Method - 3 (Top of primary stack is equivalent to rear of the queue with
# Amortized complexity of O(1):


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return (not self.s1) and (not self.s2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
