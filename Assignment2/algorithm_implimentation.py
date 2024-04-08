from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    maxprofit = 0
    mini = prices[0]
    for price in prices[1:]:
        if price < mini:
            mini = price
        else:
            maxprofit = max(maxprofit, price - mini)
    return maxprofit

# Input
prices = [7, 1, 5, 3, 6, 4, 9, 2, 8]

# Output
print(maxProfit(prices))
