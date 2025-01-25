def solucionarRompecabezas(N):
    # Definimos un módulo grande para manejar el cálculo
    MOD = 10**10  # Últimos 10 dígitos
    
    var_A = 1
    var_B = 1
    var_C = 1
    var_D = 1
    
    for _ in range(1, N+1):
        # Realizamos todos los cálculos con módulo para evitar desbordamiento
        resultado = (3 * var_D + var_C + 4 * var_B + var_A) % MOD
        var_A = var_B
        var_B = var_C
        var_C = var_D
        var_D = resultado
    
    return var_D

# Pruebas
print("solucionarRompecabezas(10):", solucionarRompecabezas(10))
print("solucionarRompecabezas(100):", solucionarRompecabezas(100))

# Cálculo para 2023^100
N = pow(2023, 100)
print("solucionarRompecabezas(2023^100):", solucionarRompecabezas(N))