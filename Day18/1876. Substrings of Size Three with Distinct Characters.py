def countGoodSubstrings(s):
    left = 0
    my_set = set()
    count = 0
    for right in range(len(s)):
        while s[right] in my_set or len(my_set) == 3:
            my_set.remove(s[left])
            left += 1
        my_set.add(s[right])
        if len(my_set) == 3:
            count += 1
    return count


def solve():
    s = "aababcabc"
    print(countGoodSubstrings(s))


if __name__ == "__main__":
    solve()
