nombre = input("Introduce tu nombre: ")
if len(nombre) == 0:
    print("Debes introducir el nombre")
else:
    apellido = input("Introduce tu apellido: ")
    if len(apellido) > 100:
        print("Has introducido muchos caracteres")
    elif len(apellido) != 0:
        cars = len(apellido) + len(nombre)
        if(cars < 5):
            print("Muy corto")
        else:
            print(f"Tu nombre completo tiene {cars} caracteres")
    else:
        print("  Apellido vacio ")
        print("        ^        ")
        print("       ^^^       ")
        print("      ^^^^^      ")
        print("     ^^^^^^^     ")
        print("    ^^^^^^^^^    ")
        print("   ^^^^^^^^^^^   ")
        print("  ^^^^^^^^^^^^^  ")
        print("       |||       ")
        print("       |||       ")