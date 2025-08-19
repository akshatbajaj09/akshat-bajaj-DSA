# Binary Search solution:
def minEatingSpeed(piles, h):
    l = 1
    r = max(piles)
    ans = r
    while l <= r:
        k = (l + r) // 2
        count = 0
        for i in range(len(piles)):
            count += (piles[i] + k - 1) // k
        if count <= h:
            ans = k
            r = k - 1
        else:
            l = k + 1
    return ans


def solve():
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))


if __name__ == "__main__":
    solve()
