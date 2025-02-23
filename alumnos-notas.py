alumnos = {}
seguir = True
while (seguir):
    print("1==> Añadir alumno y calificación")
    print("2==> Mostrar alumnos y calificación")
    print("3==> Buscar alumno y mostrar calificación")
    print("4==> Modificar calificación")
    print("5==> Eliminar alumno")
    print("6==> Calcular y mostrar promedio, calificación máxima y mínima")
    print("7==> Ordenar alumnos alfabéticamente o por calificación")
    print("8==> Salir")
    op = input("Introduce una opción a realizar: ")
    if op == "1":
        nombre = input("Introduce el nombre del alumno: ")
        calificacion = float(input("Introduce la calificación del alumno: "))
        alumnos[nombre] = calificacion
    elif op == "2":
        print("------LISTA DE ALUMNOS Y CALIFICACIONES------")
        for nombre, calificacion in alumnos.items():
            print(f"Alumno: {nombre}, Calificación: {calificacion}")
        print("--------------------------------------------")
    elif op == "3":
        nombre = input("Ingrese el nombre del alumno a buscar: ")
        if nombre in alumnos:
            print(f"La calificación de {nombre} es: {alumnos[nombre]}")
        else:
            print("Alumno no encontrado")
    elif op == "4":
        nombre = input("Ingrese el nombre del alumno para modificar su calificacion: ")
        if nombre in alumnos:
            nota = float(input("Introduce la nueva calificación del alumno: "))
            alumnos[nombre] = nota
        else:
            print("Alumno no encontrado")
    elif op == "5":
        nombre = input("Ingrese el nombre del alumno para eliminar: ")
        if nombre in alumnos:
            del(alumnos[nombre])
        else:
            print("Alumno no encontrado")
    elif op == "6":
        if len(alumnos) > 0:
            promedio = sum(alumnos.values()) / len(alumnos)
            max_calificacion = max(alumnos.values())
            min_calificacion = min(alumnos.values())
            print(f"Promedio: {promedio:.2f}")
            print(f"Calificación máxima: {max_calificacion}")
            print(f"Calificación mínima: {min_calificacion}")
        else:
            print("No hay alumnos registrados")
    elif op == "7":
        print("1==> Ordenar alfabeticamente")
        print("2==> Ordenar por calificación")
        op2 = input("Introduce una opcion: ")
        if op2 == "1":
            alumnos_ordenados = sorted(alumnos.items())
            for alumno, calificacion in alumnos_ordenados:
                print(f"Alumno: {alumno}, Calificación: {calificacion}")
        elif op2 == "2":
            lista_alumnos = list(alumnos.items())
            for i in range(len(lista_alumnos)):
                for j in range(0, len(lista_alumnos) - i - 1):
                    if lista_alumnos[j][1] > lista_alumnos[j + 1][1]:
                        lista_alumnos[j], lista_alumnos[j + 1] = lista_alumnos[j + 1], lista_alumnos[j]
            for alumno, calificacion in lista_alumnos:
                print(f"Alumno: {alumno}, Calificación: {calificacion}")
        else:
            print("Opcion no permitida")
    elif op == "8":
        seguir = False
    else:
        print("Opcion no permitida")