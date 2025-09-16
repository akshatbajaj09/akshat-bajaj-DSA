# Two sum problem (leetocode question 1):

# While storing the elements in the hashmap, I stored the complements of the given
# numbers instead of the numbers themselves, which didn't work out and hence the
# correct way to do it is by storing the numbers themselves.


def twoSum(self, nums, target):
    my_dict = {}
    for i, num in enumerate(nums):
        val = target - num
        if val not in my_dict:
            # my_dict[val] = i -> This is storing the complement, which does not work.
            my_dict[num] = i
        else:
            return [my_dict[val], i]
