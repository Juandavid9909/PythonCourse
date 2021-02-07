nombres = ["Juan", "Karla", "Ricardo", "Maria"]
print(nombres)

# Conocer el largo de la lista
print(len(nombres))
print(nombres[0])
print(nombres[1])

# Navegación inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir rango
print(nombres[0:2]) # Sin incluir el indice 2

# Imprimir los elementos de inicio hasta el indice propocionado
print(nombres[:3])

# Imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])

for nombre in nombres:
    print(nombre)
    
if "Karla" in nombres:
    print("Karla si existe en la lista")
else:
    print("El elemento buscado no existe en la lista")
    
# Agregar un nuevo elemento
nombres.append("Lorenzo")

# Insertar un nuevo elemento en el indice proporcionado
nombres.insert(1, "Octavio")
print(nombres)

# Remover un elemento
nombres.remove("Octavio")
print(nombres)

# Remover el ultimo elemento
nombres.pop()

# Remover el indice indicado de la lista
del nombres[0]

# Limpiar los elementos de nuestra lista
nombres.clear()

# Eliminar por completo la lista
del nombres