# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

def birthday(s, d, m):
    # s = [] segmentos del chocolate
    # d = int -> dia de cumple / suma
    # m = int => mes del cumple / longitud de segmento
    
    contador_segmentos_ok = 0
    
    if len(s) == 1:
        return m
    else:
        for i in range(len(s) - 1):
            aux = s[i:]
            aux2 = aux[:m]
            if sum(aux2) == d:
                contador_segmentos_ok = contador_segmentos_ok + 1
        
        return contador_segmentos_ok

# result = birthday([1, 2, 1, 3, 2], 3, 2)
# result = birthday([1, 1, 1, 1, 1, 1], 3, 2)
# result = birthday([4], 4, 1)
result = birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7)

print(result)