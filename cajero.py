saldo = 1000
seguir = True
while seguir:
    print("1. Añadir dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Salir")
    try:
        opcion = input("Selecciona una opción (1-4): ")
        if opcion == "1":
            cantidad = float(input("¿Cuánto dinero deseas añadir? "))
            saldo += cantidad
            print(f"Has añadido: {cantidad}. El saldo actual es: {saldo}.")
            
        elif opcion == "2":
            cantidad = float(input("¿Cuánto dinero deseas retirar? "))
            if cantidad <= saldo:
                saldo -= cantidad
                print(f"Has retirado: {cantidad}. El saldo actual es: {saldo}.")
            else:
                print("Saldo insuficiente.")
        elif opcion == "3": 
            print(f"El saldo actual es: {saldo}.")
            
        elif opcion == "4":
            print("¡Nos vemos!")
            seguir = False
            
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")
    except:
        print("Error con los datos introducidos.")
