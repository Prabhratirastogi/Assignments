from algorithm_implimentation import maxProfit
def test_increasing_trend():
    # Test case: Verify that the function returns the correct maximum profit for a list of stock prices with an increasing trend
    prices = [1, 2, 3, 4, 5]
    assert maxProfit(prices) == 4

def test_decreasing_trend():
    # Test case: Verify that the function returns the correct maximum profit for a list of stock prices with a decreasing trend
    prices = [5, 4, 3, 2, 1]
    assert maxProfit(prices) == 0

def test_no_profit_possible():
    # Test case: Verify that the function returns 0 if it's not possible to make a profit
    prices = [5, 4, 3, 2, 1]
    assert maxProfit(prices) == 0

def test_single_price():
    # Test case: Verify that the function returns 0 for a single price (no profit possible)
    prices = [5]
    assert maxProfit(prices) == 0

def test_empty_list():
    # Test case: Verify that the function returns 0 for an empty list
    prices = []
    assert maxProfit(prices) == 0

def test_max_profit_middle():
    # Test case: Verify that the function returns the correct maximum profit for a list of stock prices with the maximum profit in the middle
    prices = [7, 1, 5, 3, 6, 4, 9, 2, 8]
    assert maxProfit(prices) == 8

