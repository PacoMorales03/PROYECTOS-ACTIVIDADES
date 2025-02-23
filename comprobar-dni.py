dni = input("Introduce el DNI: ")
if len(dni) == 9:
    if dni[:-1].isdigit():
        if dni[-1].isalpha():
            print("El DNI es correcto.")
        else:
            print("El caracter de la letra es incorrecto.")
    else:
        print("Los primeros 8 caracteres deben ser números.")
else:
    print("EL DNI tiene que tener 9 caracteres.")
