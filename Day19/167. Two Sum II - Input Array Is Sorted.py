def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        value = numbers[left] + numbers[right]
        if value == target:
            return [left + 1, right + 1]
        elif value < target:
            left += 1
        else:
            right -= 1


def solve():
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers, target))


if __name__ == "__main__":
    solve()
