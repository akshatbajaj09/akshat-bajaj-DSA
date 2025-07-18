def maximumWealth(accounts):
    wealths = []
    for item in accounts:
        wealths.append(sum(item))
    return max(wealths)

def solve():
    accounts = [[1,2,3],[3,2,1]]
    print(maximumWealth(accounts))

if __name__ == '__main__':
    solve()