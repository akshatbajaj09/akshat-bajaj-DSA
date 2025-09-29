# Earlier we solved the Design HashSet problem by simply using a boolean array but
# as we discussed that the approach of a boolean array was only good when the range of
# the values of the keys was is known and manageable and in case having higher values
# for the keys, we should use another approach like chaining using linked lists.

# So below is the implementation of the chaining method:


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        self.my_set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.my_set[index]
        while curr.next:  # Skipping the dummy node
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.my_set[index]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hash_func(key)
        curr = self.my_set[index]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False

    def hash_func(self, key):
        return key % len(self.my_set)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# In the above implementation we simply chose an array size (10**4) that
# matches the maximum number of calls but another way which amortizes
# the overall efficiency to O(1) is by implementing rehashing which although
# isn't required in this problem as the number of calls are limited to 10**4 but
# for larger datasets which may have 10**7 or more calls, the rehashing approach
# is preferred.
