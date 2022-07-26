# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

def getTotalX(a, b):
    
    maximo = 101
    resultados = []
    
    for i in range(1, maximo):
        acumulador = 0
        
        for x in a:
            acumulador = acumulador + i%x
        
        for y in b:
            acumulador = acumulador + y%i   
            
        if acumulador == 0:
            resultados.append(i)
                                    
    return len(resultados)
        
a = [1]
b = [100]

print(getTotalX(a, b))