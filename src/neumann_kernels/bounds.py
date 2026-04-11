import math

def s_n(radix, n):
    return 0 if n <= 0 else (radix ** n - 1) // (radix - 1)

def crouzeix_bound(w_a, rho, q_rho_value, radix, step, c_cr=1.0 + math.sqrt(2.0)):
    return c_cr * rho * (q_rho_value ** s_n(radix, step)) * ((w_a / rho) ** (radix ** step))
