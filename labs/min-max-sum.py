# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=profile

def miniMaxSum(arr):
    arr.sort()
    s = sum(arr)
    maxResult = s - arr[0]
    minResult = s - arr[len(arr) - 1]
    
    print(minResult, maxResult)


miniMaxSum([769082435, 210437958, 673982045, 375809214, 380564127])
