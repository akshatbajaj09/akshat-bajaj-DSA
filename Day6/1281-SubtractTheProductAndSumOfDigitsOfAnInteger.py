def subtractProductAndSum(n):
    digits = [item for item in str(n)]
    sum_of_digits = 0
    product_of_digits = 1
    for i in range(len(digits)):
        sum_of_digits += int(digits[i])
        product_of_digits *= int(digits[i])
    return product_of_digits - sum_of_digits
    
def solve():
    n = 4421
    print(subtractProductAndSum(n))

if __name__ == '__main__':
    solve()