def fibonacci(n):
    # A partir de un entero, devuelve los primeros n numeros de Fibonacci

    arr = []
    arr.append(1)
    arr.append(1)

    for i in range(2, n):
        arr.append(arr[i-2] + arr[i-1])
    
    return arr

def is_fibonacci(arr):
    # A partir de un array de enteros, devuelve en cada posicion 1 o 0 
    # si el elemento es un numero de Fibonacci

    # Armo el array de Fibonacci hasta la posicion 100
    fibo = fibonacci(len(arr))

    # Array con los resultados
    result = []

    for i in range(0, len(arr)):
        if arr[i] in fibo:
            result.insert(i, 1)
        else:
            result.insert(i, 0)
    return result

# Pruebas:

arr = [1, 9, 2, 3, 5, 8, 33, 21, 54]
x = is_fibonacci(arr)
print(x)

