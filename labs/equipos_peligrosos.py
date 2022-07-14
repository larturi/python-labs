# Recibe un string 011111110101001
# Devuelve Yes si hay 7 consecutivos (ceros o unos)

def equiposPeligrosos(cadena):

    count_consecutives = 0

    for i in range(0, len(cadena) - 1):

        if count_consecutives != 0:
            previous_char = cadena[i-1:i]
        else:
            previous_char = cadena[i:i+1]

        char = cadena[i:i+1]

        if char == previous_char: 
            count_consecutives = count_consecutives + 1
        else:
            count_consecutives = 1

        if count_consecutives >= 7: 
            print('Equipo ' + cadena + ': Yes')
            return True

    if count_consecutives < 7:
        print('Equipo ' + cadena + ': No')
        return False

# Pruebas:
equiposPeligrosos('00101000100100')
equiposPeligrosos('01111111100000')
equiposPeligrosos('11100111010101')
equiposPeligrosos('01010101011010')
equiposPeligrosos('00101010100010')
equiposPeligrosos('11000000001111')
equiposPeligrosos('11100000001110')
equiposPeligrosos('00001100000000')
equiposPeligrosos('00001100011000')
