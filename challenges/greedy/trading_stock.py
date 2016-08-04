def max_profit_yesterday(stock_prices):
    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]

    for price in stock_prices[1:]:
        possibe_profit = price - min_price
        max_profit = max(possibe_profit, max_profit)
        min_price = min(min_price, price)

    return max_profit


def test_max_profit_yesterday_normal():
    stock_prices_yesterday = [10, 7, 5, 8, 3, 4, 10, 11, 2, 4, 5]
    assert max_profit_yesterday(stock_prices_yesterday) == 8


def test_max_profit_yesterday_crash():
    stock_prices_crash = [10, 7, 5, 1]
    assert max_profit_yesterday(stock_prices_crash) == -2
