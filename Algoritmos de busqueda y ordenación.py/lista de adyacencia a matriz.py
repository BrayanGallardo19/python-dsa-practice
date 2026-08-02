def adjacency_list_to_matrix(adj_list):
    # Determinar el número de nodos
    num_nodes = len(adj_list)

    # Crear una matriz llena de ceros
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    # Llenar la matriz según la lista de adyacencia
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Imprimir cada fila
    for row in matrix:
        print(row)

    # Devolver la matriz
    return matrix   