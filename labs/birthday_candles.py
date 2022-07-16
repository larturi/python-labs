import re


def birthdayCakeCandles(candles):
    candles_sorted = sorted(candles, reverse=True)
    max_age = candles_sorted[0]
    return candles_sorted.count(max_age)


print(birthdayCakeCandles([4, 4, 2, 3, 4, 1]))