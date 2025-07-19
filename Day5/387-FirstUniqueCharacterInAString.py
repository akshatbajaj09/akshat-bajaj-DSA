def firstUniqChar(s):
    if all(s.count(i) > 1 for i in s):
        return -1
    else:
        for item in range(len(s)):        
            if s.count(s[item]) == 1:
                return item

# TLE using above method, so trying a new one:
def firstUniqChar2(s):

    freq_dict = {}

    for item in s:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1

    for i in range(len(s)):
        if freq_dict[s[i]] == 1:
            return i
    return -1

def solve():
    s = 'loveleetcode'
    print(firstUniqChar(s))
    print(firstUniqChar2(s))

if __name__ == '__main__':
    solve()