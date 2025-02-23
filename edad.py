nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Qué edad tienes? "))
if edad < 0:
    print("No puedes tener menos de 0 años")
elif edad < 18:
    print("Menor edad")
else:
    print("Mayor edad")
    car = len(nombre)
    if  car > 10:
        print(f"Tu nombre es muy largo, tiene {car} letras")
    else:
        print(f"Tu nombre no es largo, tiene {car} letras")
