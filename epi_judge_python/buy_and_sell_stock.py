from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    curr_min = prices[0]
    profit = 0
    for i in range(len(prices)):
        curr_min = min(curr_min, prices[i])
        profit = max(profit, prices[i] - curr_min)
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
