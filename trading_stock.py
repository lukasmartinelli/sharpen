stock_prices_yesterday = [10, 7, 5, 8, 3, 4, 10, 11, 2, 4, 5]


def max_profit_yesterday(stock_prices):
    max_profit = 0
    min_price = stock_prices[0]

    for price in stock_prices:
        if price < min_price:
            min_price = price

        possibe_profit = price - min_price
        if possibe_profit > max_profit:
            max_profit = possibe_profit

    return max_profit


print(max_profit_yesterday(stock_prices_yesterday))
