#!/usr/bin/python3
"""Defines make change prototype
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0

    # Create a table to store the minimum number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Update the table based on the available coin denominations
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
