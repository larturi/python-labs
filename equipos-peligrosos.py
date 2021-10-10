# Recibe un string 011111110101001
# Devuelve Yes si hay 7 consecutivos (ceros o unos)

def equipos_peligrosos(cadena):

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
equipos_peligrosos('00101000100100')
equipos_peligrosos('01111111100000')
equipos_peligrosos('11100111010101')
equipos_peligrosos('01010101011010')
equipos_peligrosos('00101010100010')
equipos_peligrosos('11000000001111')
equipos_peligrosos('11100000001110')
equipos_peligrosos('00001100000000')
equipos_peligrosos('00001100011000')
