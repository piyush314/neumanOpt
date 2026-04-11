import numpy as np

def quinary_coeffs():
    coeffs = np.zeros(8)
    coeffs[:5] = 1.0
    return coeffs

def radix9_coeffs():
    coeffs = np.zeros(12)
    coeffs[:9] = 1.0
    return coeffs
