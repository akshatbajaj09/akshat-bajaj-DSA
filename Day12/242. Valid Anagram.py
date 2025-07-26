def isAnagram(s, t):
    if len(s) != len(t):
        return False

    freq_dict = {}
    for item in s:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1

    for item in t:
        if item not in freq_dict:
            return False
        else:
            freq_dict[item] -= 1

    for item in freq_dict:
        if freq_dict[item] != 0:
            return False

    return True


def solve():
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))


if __name__ == "__main__":
    solve()
