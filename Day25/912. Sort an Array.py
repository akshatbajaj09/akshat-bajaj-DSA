def mergeSort(nums, left, right):
    # Base case:
    if left == right:
        return
    # Recursive case:
    mid = (left + right) // 2
    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)
    # Merge:
    merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    a = nums[left : mid + 1]
    b = nums[mid + 1 : right + 1]
    i, j, k = 0, 0, left
    while k <= right:
        if i == len(a):
            nums[k] = b[j]
            j += 1
            k += 1
        elif j == len(b):
            nums[k] = a[i]
            i += 1
            k += 1
        elif a[i] < b[j]:
            nums[k] = a[i]
            i += 1
            k += 1
        else:
            nums[k] = b[j]
            j += 1
            k += 1


def sortArray(nums):
    mergeSort(nums, 0, len(nums) - 1)
    return nums


def solve():
    nums = [5, 1, 1, 2, 0, 0]
    print(sortArray(nums))


if __name__ == "__main__":
    solve()
