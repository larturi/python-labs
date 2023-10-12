def migratoryBirds(arr):
    # Crear un diccionario para contar la frecuencia de cada tipo de ave
    bird_counts = {}
    
    # Inicializar el conteo para cada tipo de ave en 0
    for bird_type in set(arr):
        bird_counts[bird_type] = 0
    
    # Contar la frecuencia de avistamientos de cada tipo de ave
    for bird_type in arr:
        bird_counts[bird_type] += 1

    # Encontrar el tipo de ave más avistado y el tipo más pequeño si hay empate
    max_count = 0
    min_type = float('inf')
    for bird_type, count in bird_counts.items():
        if count > max_count or (count == max_count and bird_type < min_type):
            max_count = count
            min_type = bird_type
    
    return min_type     

# result = migratoryBirds([9, 1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 8])
result = migratoryBirds([1, 4, 4, 4, 5, 3])

print(result)