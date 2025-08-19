# Brute force:
# Time complexity: O(m*n)
def searchMatrix(matrix, target):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if target == matrix[row][col]:
                return True
    return False


def solve():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(searchMatrix(matrix, target))


if __name__ == "__main__":
    solve()
