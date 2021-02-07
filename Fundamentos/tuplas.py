# Tupla mantiene el orden, pero ya no se puede modificar
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

# Longitud
print(len(frutas))
print(frutas[2])

# Navegación inversa
print(frutas[-1])

# Rango
print(frutas[0:2])

# No se puede modificar a no ser que se convierta la tupla en una lista
frutasLista = list(frutas)
frutas = tuple(frutasLista)

for fruta in frutas:
    print(fruta, end = " ")
    
del frutas