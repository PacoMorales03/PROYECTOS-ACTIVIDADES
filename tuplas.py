#Una tupla es invariable, a no ser que se le vuelvan a asignar valores
diasSemana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
op = int(input("Introduce el dia: ")) -1
if( 0 <= op <= 4):
    print(f"El {diasSemana[op]} es laborable")
else:
    print(f"El {diasSemana[op]} es no laborable")
