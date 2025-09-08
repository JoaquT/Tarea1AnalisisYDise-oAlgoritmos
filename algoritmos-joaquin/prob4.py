import math

# -------- Utilidades --------
def next_power_of_two(n: int) -> int:
    """Retorna la siguiente potencia de 2 mayor o igual a n."""
    return 1 if n == 0 else 2**math.ceil(math.log2(n))

def pad_matrix(A: list, size: int) -> list:
    """Rellena la matriz A con ceros hasta ser size x size."""
    n = len(A)
    m = len(A[0])
    return [row + [0]*(size-m) for row in A] + [[0]*size for _ in range(size-n)]

def unpad_matrix(A: list, rows: int, cols: int) -> list:
    """Recorta la matriz A al tamaño original."""
    return [row[:cols] for row in A[:rows]]

def add_matrix(A: list, B: list) -> list:
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A: list, B: list) -> list:
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(A: list):
    """Divide una matriz en 4 cuadrantes."""
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

# -------- Multiplicación recursiva --------
def mult_divide_conquer(A: list, B: list) -> list:
    n = len(A)
    # Caso base: 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Dividir matrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    # Calcular subproductos recursivos
    C11 = add_matrix(mult_divide_conquer(A11, B11), mult_divide_conquer(A12, B21))
    C12 = add_matrix(mult_divide_conquer(A11, B12), mult_divide_conquer(A12, B22))
    C21 = add_matrix(mult_divide_conquer(A21, B11), mult_divide_conquer(A22, B21))
    C22 = add_matrix(mult_divide_conquer(A21, B12), mult_divide_conquer(A22, B22))
    
    # Combinar resultados
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

# -------- Función general --------
def multiply_general(A: list, B: list) -> list:
    """Multiplica matrices A (n×m) y B (m×p) usando divide y vencerás."""
    n, m, p = len(A), len(A[0]), len(B[0])
    if len(B) != m:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")
    
    # Padding al siguiente tamaño potencia de 2
    size = next_power_of_two(max(n, m, p))
    A_pad = pad_matrix(A, size)
    B_pad = pad_matrix(B, size)
    
    # Multiplicación recursiva
    C_pad = mult_divide_conquer(A_pad, B_pad)
    
    # Recortar al tamaño original
    return unpad_matrix(C_pad, n, p)

# -------- Ejemplo de uso --------
if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6]
         ]
    
    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]
    
    C = multiply_general(A, B)
    
    print("Matriz A:")
    for fila in A: print(fila)
    print("\nMatriz B:")
    for fila in B: print(fila)
    print("\nResultado A*B:")
    for fila in C: print(fila)
