def mySqrt(x):
    l = 0
    r = x
    while l <= r:
        mid = (l + r) // 2
        mid_squared = mid * mid
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


def solve():
    x = 20
    print(mySqrt(x))


if __name__ == "__main__":
    solve()
