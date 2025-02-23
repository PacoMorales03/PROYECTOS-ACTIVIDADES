# Diccionario para almacenar la información de los alumnos
alumnos = {}

def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    if nombre in alumnos:
        print("Error: Ya existe un alumno con ese nombre.")
        return
    edad = int(input("Ingrese la edad del alumno: "))
    notas = []
    seguir = True
    while seguir:
        nota = float(input("Ingrese una calificación (o -1 para terminar): "))
        if nota == -1:
            seguir = False
        notas.append(nota)
    alumnos[nombre] = {"edad": edad, "notas": notas}
    print("Alumno agregado con éxito.")

def mostrar_todos_los_alumnos():
    for nombre, datos in alumnos.items():
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Promedio: {promedio:.2f}")

def buscar_alumno():
    nombre = input("Ingrese el nombre del alumno a buscar: ")
    if nombre in alumnos:
        datos = alumnos[nombre]
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Notas: {datos['notas']}, Promedio: {promedio:.2f}")
    else:
        print("Error: No se encontró el alumno.")

def editar_datos_de_alumno():
    nombre = input("Ingrese el nombre del alumno a editar: ")
    if nombre in alumnos:
        datos = alumnos[nombre]
        print("1. Editar nombre")
        print("2. Editar edad")
        print("3. Editar notas")
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            alumnos[nuevo_nombre] = datos
            del alumnos[nombre]
        elif opcion == 2:
            nueva_edad = int(input("Ingrese la nueva edad: "))
            datos["edad"] = nueva_edad
        elif opcion == 3:
            notas = []
            seguir = True
            while seguir:
                nota = float(input("Ingrese una calificación (o -1 para terminar): "))
                if nota == -1:
                    seguir = False
                notas.append(nota)
            datos["notas"] = notas
        print("Datos editados con éxito.")
    else:
        print("Error: No se encontró el alumno.")

def eliminar_alumno():
    nombre = input("Ingrese el nombre del alumno a eliminar: ")
    if nombre in alumnos:
        del alumnos[nombre]
        print("Alumno eliminado con éxito.")
    else:
        print("Error: No se encontró el alumno.")

def estadisticas_de_la_clase():
    if not alumnos:
        print("No hay alumnos en la clase.")
        return
    total_alumnos = len(alumnos)
    promedio_general = 0
    for datos in alumnos.values():
        promedio_general += sum(datos["notas"]) / len(datos["notas"])
    promedio_general /= total_alumnos
    alumno_con_promedio_mas_alto = None
    alumno_con_promedio_mas_bajo = None
    promedio_mas_alto = -1000
    promedio_mas_bajo = 1000
    for nombre, datos in alumnos.items():
        promedio = sum(datos["notas"]) / len(datos["notas"])
        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            alumno_con_promedio_mas_alto = nombre
        if promedio < promedio_mas_bajo:
            promedio_mas_bajo = promedio
            alumno_con_promedio_mas_bajo = nombre
    print(f"Total de alumnos: {total_alumnos}")
    print(f"Promedio general: {promedio_general:.2f}")
    print(f"Alumno con promedio más alto: {alumno_con_promedio_mas_alto}")
    print(f"Alumno con promedio más bajo: {alumno_con_promedio_mas_bajo}")

seguir = True
while seguir:
    print("Menú:")
    print("1. Agregar un alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Buscar un alumno")
    print("4. Editar los datos de un alumno")
    print("5. Eliminar un alumno")
    print("6. Estadísticas de la clase")
    print("7. Salir del programa")
    opcion = int(input("Ingrese la opción: "))
    if opcion == 1:
        agregar_alumno()
    elif opcion == 2:
        mostrar_todos_los_alumnos()
    elif opcion == 3:
        buscar_alumno()
    elif opcion == 4:
        editar_datos_de_alumno()
    elif opcion == 5:
        eliminar_alumno()
    elif opcion == 6:
        estadisticas_de_la_clase()
    elif opcion == 7:
        seguir = False
    else:
        print("Error: Opción inválida")