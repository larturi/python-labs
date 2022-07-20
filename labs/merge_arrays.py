def mergeArrays(a, b):
    c = []
    largo_a = len(a)
    largo_b = len(b)
    i = 0
    j = 0
    
    while len(c) < largo_a + largo_b:
        
        if i < largo_a and j < largo_b:
            if a[i] < b[j]:
                c.append(a[i])
                i += 1

            else:
                c.append(b[j])
                j += 1
            
        elif i == largo_a:
            c.append(b[j])
            j += 1
            
        elif j == largo_b:
            c.append(a[i])
            i += 1
            
    return c

print(mergeArrays([1, 3, 5, 7, 9, 11, 11, 13], [2, 4, 6, 6, 11, 13]))