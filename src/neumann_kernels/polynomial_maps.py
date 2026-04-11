import numpy as np

from .circuit_ansatz import evaluate_bilinear_kernel

def error_map_coefficients(poly_coeffs, radix, tol=1e-15):
    coeffs = {}
    degree = len(poly_coeffs) - 1
    for j in range(radix, degree + 1):
        coeff = poly_coeffs[j - 1] - poly_coeffs[j]
        if abs(coeff) > tol:
            coeffs[j] = float(coeff)
    if abs(poly_coeffs[degree]) > tol:
        coeffs[degree + 1] = float(poly_coeffs[degree])
    return coeffs

def eta_rho(error_map, rho):
    return float(sum(abs(c) * rho ** (j - 1) for j, c in error_map.items()))

def q_rho(error_map, rho, npts=32768):
    theta = np.linspace(0.0, 2.0 * np.pi, npts, endpoint=False)
    z = rho * np.exp(1j * theta)
    values = np.zeros_like(z, dtype=complex)
    for degree, coeff in error_map.items():
        values += coeff * z ** degree
    return float(np.max(np.abs(values)) / rho)

def error_map_from_params(params, radix, num_products, max_deg=70):
    poly = evaluate_bilinear_kernel(params, num_products, max_deg=max_deg)
    return error_map_coefficients(poly, radix)
