
def maximaDiferencia(a):
    
    diff = -1
    
    large = len(a)
    
    if large == 0:
        return diff
    
    for x in range(large - 1):
        for y in range(x+1, large):
            if a[y] > a[x]:
                diff = max(diff, a[y] - a[x])
    
    return diff
    
print(maximaDiferencia([15, 3, 6, 10]))