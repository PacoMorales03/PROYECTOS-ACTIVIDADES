nombrEstudiantes = []
notas = []
try:
    numEst = int(input("Introduce el número de estudiantes de una clase: "))
    for i in range (numEst):
        nombre = input("Itroduce el nombre del estudiante: ")
        nota = float(input("Introduce la nota del estudiante: "))
        nombrEstudiantes.append(nombre)
        notas.append(nota)
    alta = max(notas)
    baja = min(notas)
    media = sum(notas)/numEst
    print("Estos son los resultados obtenidos por la clase: ")
    print(f"La nota más alta es: {alta:.2f}")
    print(f"La nota más baja es: {baja:2f}")
    print(f"Promedio de las notas: {media:.2f}")
    print("Listado de estudiantes y sus notas:")
    for nombre, nota in zip(nombrEstudiantes, notas):
        print(f"{nombre}: {nota}")
except:
    print("Error con los datos introducidos.")

