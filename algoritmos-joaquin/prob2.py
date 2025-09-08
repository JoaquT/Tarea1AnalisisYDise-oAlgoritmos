import random as r

def merge_freq(freq_izq: dict, freq_der: dict) -> dict:
    combinado = freq_izq.copy()
    for k, v in freq_der.items():
        combinado[k] = combinado.get(k, 0) + v
    return combinado

def moda_divide_venceras(arr):
    if len(arr) == 1:
        return {arr[0]: 1}  

    mid = len(arr) // 2

    freq_izq = moda_divide_venceras(arr[:mid])
    freq_der = moda_divide_venceras(arr[mid:])

    return merge_freq(freq_izq, freq_der)

def encontrar_modas(arr):
    conteo = moda_divide_venceras(arr)

    max_freq = max(conteo.values())
    modas = [x for x, f in conteo.items() if f == max_freq]
    return modas, max_freq

numeros = [r.randint(1, 10) for _ in range(r.randint(5, 12))]
print("Lista:", numeros)
modas, freq = encontrar_modas(numeros)
print("Moda(s):", modas, "con frecuencia", freq)
