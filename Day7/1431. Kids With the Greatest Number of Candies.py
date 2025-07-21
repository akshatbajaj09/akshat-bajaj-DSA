def kidsWithCandies(candies, extraCandies):
    greatest_no_of_candies = max(candies)
    result = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= greatest_no_of_candies:
            result.append(True)
        else: 
            result.append(False)
    return result

def solve():
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))

if __name__ == '__main__':
    solve()