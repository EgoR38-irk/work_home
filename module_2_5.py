def get_matrix(n, m, value):
    matrix = []
    for n in range(n):
        matrix.append([])
        for i in range(m):
            matrix[n].append(value)
    print(matrix)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
