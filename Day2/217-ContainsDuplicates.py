
def containsDuplicate(nums):
    empty_set = set()
    for item in nums:
        if item in empty_set:
            return True
        empty_set.add(item)
    return False

def solve():
    nums = [1,2,3,1]
    print(containsDuplicate(nums))

if __name__ == '__main__':
    solve()