def maxProfit(prices):
    left, right = 0, 1
    current_profit, total_profit = 0, 0
    # left: buy and right: sell
    while right < len(prices):
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            total_profit += current_profit
        left = right
        right += 1
    return total_profit


def solve():
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))


if __name__ == "__main__":
    solve()
