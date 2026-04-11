try:
    import scipy.optimize as spo
except Exception as exc:  # pragma: no cover
    spo = None
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None

def require_scipy():
    if spo is None:
        raise RuntimeError("SciPy is required for search workflows") from _IMPORT_ERROR
    return spo
