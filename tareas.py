seguir = True
tareas=["Sacar basura", "Lavar coche"]
while (seguir):
    op = int(input("1==> Mostrar todas las tareas\n2==> Agregar una nueva tarea\n3==> Marcar una tarea como completada\n4==> Salir del programa\n"))
    if(op == 1):
        print("------LISTA DE TAREAS------")
        for i in range(len(tareas)):
            print(tareas[i])
        print("---------------------------")
    elif(op == 2):
        tareas.insert(len(tareas),input("Tarea a añadir==> "))
    elif(op == 3):
        tareas.remove(input("Tarea completada==> "))
    elif(op == 4):
        seguir = False
    else:
        print("Operación no permitida.")