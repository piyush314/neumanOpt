import numpy as np

from .circuit_ansatz import evaluate_bilinear_kernel

def matrix_polynomial(coeffs, matrix):
    ident = np.eye(matrix.shape[0])
    result = np.zeros_like(matrix)
    power = ident.copy()
    for coeff in coeffs:
        if abs(coeff) > 0:
            result = result + coeff * power
        power = power @ matrix
    return result

def matrix_residual_norm(a_matrix, params, num_products, steps):
    ident = np.eye(a_matrix.shape[0])
    m_matrix = ident - a_matrix
    y = ident.copy()
    r = a_matrix.copy()
    coeffs = evaluate_bilinear_kernel(params, num_products)
    for _ in range(steps):
        y = y @ matrix_polynomial(coeffs, r)
        r = ident - m_matrix @ y
    return float(np.linalg.norm(r, 2))
