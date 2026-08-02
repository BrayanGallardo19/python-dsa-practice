def dfs(adjacency_matrix, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            # Agregar los vecinos en orden inverso para que
            # el recorrido respete el orden de los nodos.
            for neighbor in range(len(adjacency_matrix[node]) - 1, -1, -1):
                if adjacency_matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited