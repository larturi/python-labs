def diagonalDifference(arr):
    
    sum_diag_1 = 0
    sum_diag_2 = 0
    
    for i in range(len(arr)):
        sum_diag_1 += arr[i][i]
        
    for j in range(len(arr)):
        sum_diag_2 += arr[j][len(arr) - j - 1]

    return abs(sum_diag_1 - sum_diag_2)


x = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
result = diagonalDifference(x)
print(result)