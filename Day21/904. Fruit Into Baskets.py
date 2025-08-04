def totalFruit(fruits):
    freq_dict = {}
    left, total, ans = 0, 0, 0
    for right in range(len(fruits)):
        if fruits[right] not in freq_dict:
            freq_dict[fruits[right]] = 1
        else:
            freq_dict[fruits[right]] += 1
        total += 1

        while len(freq_dict) > 2:
            freq_dict[fruits[left]] -= 1
            total -= 1
            if freq_dict[fruits[left]] == 0:
                freq_dict.pop(fruits[left])
            left += 1

        ans = max(ans, total)

    return ans


def solve():
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(totalFruit(fruits))


if __name__ == "__main__":
    solve()
