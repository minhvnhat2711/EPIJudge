from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    curr_min = prices[0]
    max_index = 0
    profit = 0
    for i in range(len(prices)):
        curr_min = min(curr_min, prices[i])
        if prices[i] - curr_min > profit:
            max_index, profit = i, prices[i] - curr_min
    print(max_index)
    result = profit
    profit = 0
    curr_min = prices[max_index+1]
    for i in range(max_index+1, len(prices)):
        curr_min = min(curr_min, prices[i])
        if prices[i] - curr_min > profit:
            profit = prices[i] - curr_min
    return result + profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
