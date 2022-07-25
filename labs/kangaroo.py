import sys

def kangaroo(x1, v1, x2, v2):

    saltos_k1 = []
    saltos_k2 = []
    i = x1
    j = x2
        
    continuar = True
    iteration = 0
    
    while continuar:
        saltos_k1.append(i)
        i = i + v1
        
        saltos_k2.append(j)
        j = j + v2
                
        if (saltos_k1[iteration] == saltos_k2[iteration]):
            continuar = False
            return "YES"
            
        if v1 > v2 and saltos_k1[iteration] > saltos_k2[iteration]:
            continuar = False
            return "NO"
            
        if v2 > v1 and saltos_k2[iteration] > saltos_k1[iteration]:
            continuar = False
            return "NO"
        
        if v2 == v1 and saltos_k2[iteration] > saltos_k1[iteration]:
            continuar = False
            return "NO"
            
        iteration = iteration + 1
    
# kangaroo(0, 3, 4, 2)
# kangaroo(0, 2, 5, 3)
print (kangaroo(43, 2, 70, 2))

