def multiplicacion(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x1, x0 = divmod(x, 10**m)
    y1, y0 = divmod(y, 10**m)

    z2 = multiplicacion(x1, y1)          
    z0 = multiplicacion(x0, y0)          
    z1 = multiplicacion(x1 + x0, y1 + y0) - z2 - z0

    return z2 * 10**(2*m) + z1 * 10**m + z0


a = 12345678
b = 87654321

print(f"Multiplicación normal: {a*b}")
print(f"multiplicacion:            {multiplicacion(a,b)}")
