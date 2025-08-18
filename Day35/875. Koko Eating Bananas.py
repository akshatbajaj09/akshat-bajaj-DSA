def minEatingSpeed(piles, h):
    k = 1
    mx = max(piles)
    count = 0
    while k <= mx:
        count = 0
        for i in range(len(piles)):
            if piles[i] <= k:
                count += 1
            else:
                if piles[i] % k == 0:
                    count += piles[i] // k
                else:
                    count += (piles[i] // k) + 1
        if count <= h:
            return k
        k += 1


def solve():
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))


if __name__ == "__main__":
    solve()
