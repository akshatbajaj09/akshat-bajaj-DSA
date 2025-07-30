def isPalindrome(s):
    new_s = []

    for char in s:
        if "A" <= char <= "Z" or "a" <= char <= "z" or "0" <= char <= "9":
            new_s.append(char)
    new_s = "".join(new_s)
    new_s = new_s.lower()

    left, right = 0, len(new_s) - 1
    while left < right:
        if new_s[left] == new_s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


# Method - 2:
def isPalindrome2(s):
    new_s = ""

    for char in s:
        if "A" <= char <= "Z" or "a" <= char <= "z" or "0" <= char <= "9":
            new_s += char.lower()
    return new_s == new_s[::-1]


# Method - 3:
def isPalindrome3(s):
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()
    return new_s == new_s[::-1]


# Method - 4:
def alphanum(char):
    if "A" <= char <= "Z" or "a" <= char <= "z" or "0" <= char <= "9":
        return True
    return False


def isPalindrome4(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not alphanum(s[left]):
            left += 1
            continue
        if not alphanum(s[right]):
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def solve():
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    print(isPalindrome2(s))
    print(isPalindrome3(s))
    print(isPalindrome4(s))


if __name__ == "__main__":
    solve()
