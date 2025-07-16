# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

def SortedSquares(nums):
    squares = [i ** 2 for i in nums]
    squares.sort()
    return squares

def solve():
    nums = [-4,-1,0,3,10]
    ans = SortedSquares(nums)
    print(ans)

if __name__ == "__main__":
    solve()
