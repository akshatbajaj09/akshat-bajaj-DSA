def countDigits(num):
    count = 0
    digits = [item for item in str(num)]
    for item in digits:
        if num % int(item) == 0:
            count += 1
    return count

def solve():
    num = 1248
    print(countDigits(num))

if __name__ == '__main__':
    solve()