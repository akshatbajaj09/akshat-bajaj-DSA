def spiralOrder(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    ans = []
    while left < right and top < bottom:
        # for top row(left to right):
        for i in range(left, right):
            ans.append(matrix[top][i])
        top += 1
        # for right col(top to bottom):
        for i in range(top, bottom):
            ans.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # for bottom row(right to left):
        for i in range(right - 1, left - 1, -1):
            ans.append(matrix[bottom - 1][i])
        bottom -= 1
        # for left col(bottom to top):
        for i in range(bottom - 1, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1
    return ans


def solve():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralOrder(matrix))


if __name__ == "__main__":
    solve()
