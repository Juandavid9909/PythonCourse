# Set es una colección sin orden, no se permite elementos repetidos y no se pueden modificar (sólo agregar nuevos o eliminar)
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas))

# Revisar si un elemento está presente
print("Marte" in planetas)

# Agregar
planetas.add("Tierra")
planetas.add("Tierra")
print(planetas)

# Eliminar
planetas.remove("Tierra")
print(planetas)
planeta.discard("Jupiter") # no lanza exepciones
print(planetas)

del planetas