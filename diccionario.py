diccionario={
    "Nombre":"Roberto",
    "Edad":18,
    "Ocupacion":"Jugador"
}
'''
print(diccionario["Edad"])
del(diccionario["Edad"])
print(diccionario)
diccionario.pop("Nombre")
print(diccionario)
'''
for clave,valor in diccionario.items():
    print(f"El campo {clave} es {valor}") 

