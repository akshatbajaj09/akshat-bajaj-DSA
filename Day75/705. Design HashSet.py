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

# What we did here?:
# We made a boolean array initialized to False for all the keys, using the keys as
# indices as they were all integers.
# Now whenever the add operation takes place we change the boolean value for that
# key's index to True, similarly for removing we change the value to False if it was True
# and if the element wasn't present then after the remove operation the False is replaced
# by False again.
# For the contains operation we simply lookup at the value of the corresponding index and
# return that boolean value.

# In the above solution all operations(add, remove, and contains) have a time complexity
# of O(1) but in this case the space complexity is O(N) where N is the maximum possible
# value of the key and not the number of keys inserted.

# Hence this solution is good only in cases when the range of key values is known and
# manageable.

# For more larger values of keys we should use a different approach like chaining using
# linked lists.
