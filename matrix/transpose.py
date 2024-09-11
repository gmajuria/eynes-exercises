def transpose(matrix):
    new_matrix = []
    for column in range(len(matrix[0])):
        vector = []
        for row in range(len(matrix)):
            vector.append(matrix[row][column])
        new_matrix.append(vector)
    return new_matrix
