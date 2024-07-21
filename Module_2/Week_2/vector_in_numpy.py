import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.dot(vector, vector))
    return len_of_vector


def computer_dot_product(vector):
    result = np.sum(vector*vector)
    return result


def matrix_multi_vector(matrix, vector):
    height, width = matrix.shape
    result = np.zeros([height])
    for i in range(height):
        result[i] = np.dot(matrix[i], vector)
    return result


def inverse_matrix(matrix):
    height, width = matrix.shape
    if height != width:
        return
    else:
        det = (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
        matrix_A = [[matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]]
    return matrix_A/det


def compute_cosine(x, y):
    dot_product = np.sum(x*y)
    length_x = np.sqrt(np.sum(x*x))
    length_y = np.sqrt(np.sum(y*y))
    return dot_product/(length_x*length_y)
