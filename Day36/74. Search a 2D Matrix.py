# Method - 1 (Brute force):
# Time complexity: O(m*n)
def searchMatrix(matrix, target):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if target == matrix[row][col]:
                return True
    return False


# Method - 2 (Binary Search):
# Time complexity: O(log(m * n))
def searchMatrix2(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    l = 0
    r = (row * col) - 1

    while l <= r:
        mid = (l + r) // 2
        i = mid // col
        j = mid % col
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


def solve():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(searchMatrix(matrix, target))
    print(searchMatrix2(matrix, target))


if __name__ == "__main__":
    solve()
