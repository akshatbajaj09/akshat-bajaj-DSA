# Method - 1 (Separate chaining without rehashing):


class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0) for i in range(10**4)]

    def hash_func(self, key):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        index = self.hash_func(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash_func(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Method - 2 (Separate chaining with rehashing):


class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.capacity = 16
        self.count = 0
        self.load_threshold = 0.75
        self.hashmap = [ListNode(0) for i in range(self.capacity)]

    def hash_func(self, key):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        index = self.hash_func(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)
        self.count += 1

        if self.count / self.capacity > self.load_threshold:
            self.rehash()

    def get(self, key: int) -> int:
        index = self.hash_func(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.count -= 1
                return
            curr = curr.next

    def rehash(self):
        old_map = self.hashmap
        self.capacity *= 2
        self.count = 0
        self.hashmap = [ListNode(0) for i in range(self.capacity)]
        for bucket in old_map:
            curr = bucket
            while curr.next:
                self.put(curr.next.key, curr.next.val)
                curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
