from decimal import *
getcontext().prec = 1

def plusMinus(arr):
    positiveCounter = 0
    negetiveCounter = 0
    zeroCounter = 0

    for i in range (len(arr)):
        if arr[i] > 0:
            positiveCounter += 1
        elif arr[i] < 0 :
            negetiveCounter += 1
        else:
            zeroCounter += 1

    print("%f"%(positiveCounter / len(arr)))
    print("%f"%(negetiveCounter / len(arr)))
    print("%f"%(zeroCounter / len(arr)))

    
x = [1, 1, 0, -1, -1]
plusMinus(x)

