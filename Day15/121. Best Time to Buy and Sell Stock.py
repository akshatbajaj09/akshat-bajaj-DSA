def maxProfit(prices):
    left, right = 0, 1
    # left: buy and right: sell
    current_profit, max_profit = 0, 0
    while right < len(prices):
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
        else:
            left = right
        right += 1
    return max_profit


def solve():
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))


if __name__ == "__main__":
    solve()
