def lengthOfLongestSubstring(s):
    left = 0
    my_set = set()
    ans = 0
    for right in range(len(s)):
        while s[right] in my_set:
            my_set.remove(s[left])
            left += 1
        my_set.add(s[right])
        ans = max(ans, len(my_set))
    return ans


def solve():
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))


if __name__ == "__main__":
    solve()
