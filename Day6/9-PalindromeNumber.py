def isPalindrome(x):
    if x < 0:
        return False
    left = 0
    right = len(str(x)) - 1
    while left < right:
        if (str(x))[left] != (str(x))[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
            
# Method-2:
def isPalindrome2(x):
    str1 = str(x)
    str2 = (str(x))[::-1]
    return str1 == str2
    
def solve():
    x = 12321
    print(isPalindrome(x))
    print(isPalindrome2(x))

if __name__ == '__main__':
    solve()
