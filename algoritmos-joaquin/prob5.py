def max_sum(arr, left, mid, right):
    # Mejor suma hacia la izquierda
    sum_left = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        sum_left = max(sum_left, total)

    # Mejor suma hacia la derecha
    sum_right = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        sum_right = max(sum_right, total)

    return sum_left + sum_right


def max_subarray(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    # Caso izquierda, derecha, cruzada
    max_left = max_subarray(arr, left, mid)
    max_right = max_subarray(arr, mid + 1, right)
    max_cross = max_sum(arr, left, mid, right)

    return max(max_left, max_right, max_cross)


# Ejemplo
arr = [2, -4, 3, -1, 2, -4, 3]
resultado = max_subarray(arr, 0, len(arr) - 1)
print("Máxima suma de subsecuencia:", resultado)
