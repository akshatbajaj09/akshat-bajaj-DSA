def countOdds(low,high):
    count = 0
    difference = high - low
    if low % 2 == 0 and high % 2 == 0:
        count = difference // 2
    elif low % 2 != 0 and high % 2 != 0:
        count = (difference // 2) + 1
    else:
        count = (difference + 1) // 2
    return count
    
def solve():
    low = 3
    high = 7
    print(countOdds(low,high))

if __name__ == '__main__':
    solve()