import json
datos = {
    "nombre" : "Paco",
    "edad" : 21,
    "ciudad" : "Utrera"
}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent = 4)
print(datos)

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
print(datos)
#Añadir al diccionario
datos["profesion"] = "Estudiante"

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent = 4)
print(f"El diccionario final es: {datos}")