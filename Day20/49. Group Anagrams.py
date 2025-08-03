def sortedString(s):
    list_of_chars = [char for char in s]
    list_of_chars.sort()
    return "".join(list_of_chars)


def groupAnagrams(strs):
    my_dict = {}
    for s in strs:
        key = sortedString(s)
        if key not in my_dict:
            my_dict[key] = [s]
        else:
            my_dict[key].append(s)
    return list(my_dict.values())


# Method - 2:


def groupAnagrams2(strs):
    my_dict = {}
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        if tuple(count) not in my_dict:
            my_dict[tuple(count)] = [s]
        else:
            my_dict[tuple(count)].append(s)
    return list(my_dict.values())


def solve():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
    print(groupAnagrams2(strs))


if __name__ == "__main__":
    solve()
