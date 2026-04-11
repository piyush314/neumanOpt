import numpy as np

def evaluate_bilinear_kernel(params, num_products, max_deg=70):
    params = np.asarray(params)
    dtype = complex if np.iscomplexobj(params) else float
    ident = np.zeros(max_deg, dtype=dtype)
    ident[0] = 1
    bpoly = np.zeros(max_deg, dtype=dtype)
    bpoly[1] = 1
    basis = [ident, bpoly, np.convolve(bpoly, bpoly)[:max_deg]]
    idx = 0
    for step in range(2, num_products + 1):
        basis_size = step + 1
        left = sum(c * p for c, p in zip(params[idx:idx + basis_size], basis))
        idx += basis_size
        right = sum(c * p for c, p in zip(params[idx:idx + basis_size], basis))
        idx += basis_size
        basis.append(np.convolve(left, right)[:max_deg])
    final = params[idx:idx + num_products]
    result = ident.copy()
    for j in range(num_products):
        result = result + final[j] * basis[j + 1]
    return result + basis[-1]
