# Given an array nums of integers, return how many of them
# contain an even number of digits.

def EvenNumberOfDigits(sample_list):
        number_of_digits = 0
        count = 0
        for num in sample_list:
            number_of_digits = len(str(num))
            if number_of_digits % 2 == 0:
                count += 1
        return count

def solve():
    sample_list = [12,345,2,6,7896]
    result = EvenNumberOfDigits(sample_list) 
    print('Numbers having even number of digits are: ', result)

if __name__ == '__main__':
    solve()