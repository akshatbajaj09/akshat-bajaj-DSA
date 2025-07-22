def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n > 0:
        if n == 1:
            return True
        rem = n % 2
        if rem == 1:
            return False
        n //= 2

# Trying it via Recursion:
def recursive_func(n):
    if n <= 0:
        return False
    else:
        if n == 1:
            return True
        rem = n % 2
        if rem == 1:
            return False
        return recursive_func(n // 2)


def solve():
    n = 77
    print(isPowerOfTwo(n))
    print(recursive_func(n))

if __name__ == '__main__':
    solve()