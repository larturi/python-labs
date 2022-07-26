# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=profile

import re

def compareTriplets(a, b):
    a_wins = 0
    b_wins = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            a_wins += 1
        elif a[i] < b[i]:
            b_wins += 1
        else:
           pass

    return [a_wins, b_wins]

a = [1, 2, 3, 5, 3, 6, 7, 6, 5, 4]
b = [3, 2, 1, 1, 1, 2, 3, 4, 5, 4]
result = compareTriplets(a, b)

print(result)