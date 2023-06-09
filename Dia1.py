#Encontrar al elfo con la mayor cantidad de calorias 
#Son 5 elfos, llevan calorias de formas separadas

lista = [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000]
]

# Sumar las calorias de cada elfo
resultados = []
for sublist in lista:
    suma = sum(sublist)
    resultados.append(suma)

# Encontrar el mayor numero de calorias
resultado_mayor = max(resultados)


# elfo con mayor cantidad de calorias
elfo_calorico = resultados.index(resultado_mayor) 

# Mostrar los resultados de las operaciones
print("Suma de calorias por elfo:", resultados)
print("Resultado mayor de calorias por elfo:", resultado_mayor)
print("elfo con mayor cantidad de calorias", elfo_calorico)
