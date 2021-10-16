def kaprekar(n, loops = 10):
    # Consiste en reordenar los digitos de un numero 
    # de modo que se obtenga el mayor y el menor posible, 
    # restando entonces el menor del mayor una cantidad
    # finita de veces y siempre llega a 6174

    mayor = sorted_max(n)
    menor = sorted_min(n)
    loops = loops - 1
    result = []

    if loops > 0:
        print(str(10-loops) + '  ' + str(mayor - menor))
        result.append(mayor - menor)
        kaprekar(mayor - menor, loops)
    else:
        print('')


def sorted_max(n):
    s = list(str(n))
    s.sort(reverse = True)
    sorted_num = ''.join(s)
    return int(sorted_num)

def sorted_min(n):
    s = list(str(n))
    s.sort()
    sorted_num = ''.join(s)
    return int(sorted_num)

# Pruebas:
n = 4231
result = kaprekar(n)

