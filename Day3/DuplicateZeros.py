def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    zeros = arr.count(0)
    i = len(arr) - 1
    j = i + zeros
    while i!=j:
        if j < len(arr):
            arr[j] = arr[i]
        j -= 1 
        if arr[i] == 0:
            if j < len(arr):
                arr[j] = arr[i]   
            j -= 1
        i -= 1

def solve():
    arr = [1,0,2,3,0,4,5,0]
    duplicateZeros(arr)
    print(arr)

if __name__ == '__main__':
    solve()
