# Un diccionaro está compuesto por una llave y su valor (key, value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)
print(len(diccionario))
print(diccionario["IDE"])
print(diccionario.get("IDE"))

diccionario["IDE"] = "Integrated development environment"

for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)
    
# Comprobar si un elemento existe
print("IDE" in diccionario)

# Agregar nuevos elementos
diccionario["PK"] = "Primary Key"

# Remover elementos
diccionario.pop("DBMS")

# Limpiar
diccionario.clear()

# Eliminar
del diccionario