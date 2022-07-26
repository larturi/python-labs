# https://www.hackerrank.com/challenges/a-very-big-sum?h_r=profile

from unittest import result

def aVeryBigSum(ar):
    suma = 0
    for i in range(len(ar)):
        suma += ar[i]
        
    return suma



x = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = aVeryBigSum(x)
print(result)