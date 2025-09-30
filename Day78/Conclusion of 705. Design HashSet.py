# Method - 1 (Boolean array):


class MyHashSet:

    def __init__(self):
        self.array = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.array[key] = True

    def remove(self, key: int) -> None:
        self.array[key] = False

    def contains(self, key: int) -> bool:
        return self.array[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Method - 2 (Separate chaining without rehahsing):


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(0) for i in range(10**4)]

    def hash_func(self, key):
        return key % len(self.hash_set)

    def add(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.hash_set[index]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.hash_set[index]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hash_func(key)
        curr = self.hash_set[index]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Method - 3 (Separate chaining with rehashing):


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.capacity = 16
        self.count = 0
        self.load_threshold = 0.75
        self.hash_set = [ListNode(0) for i in range(self.capacity)]

    def hash_func(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.hash_set[index]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)
        self.count += 1

        if self.count / self.capacity > self.load_threshold:
            self.rehash_func()

    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.hash_set[index]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                self.count -= 1
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hash_func(key)
        curr = self.hash_set[index]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False

    def rehash_func(self):
        old_set = self.hash_set
        self.capacity *= 2
        self.count = 0
        self.hash_set = [ListNode(0) for i in range(self.capacity)]
        for bucket in old_set:
            curr = bucket
            while curr.next:
                self.add(curr.next.val)
                curr = curr.next


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Analysis:
# For this particular problem method 1 is most efficient then method - 2 and then
# method - 3, but in general for large scale problems, method - 3 is considered the best.
