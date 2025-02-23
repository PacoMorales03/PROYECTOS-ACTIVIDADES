print("Hola mundo")
nombre = input("¿Cómo te llamas? ")
apellido = input(f"Introduce tu apellido {nombre} ")
altura = float(input(f"¿Cuánto mides {nombre} {apellido}? "))
if altura > 1.90:
    print("Eres muy alto")
elif altura < 1.50:
    print("Que bajito")
else:
    print("Tu altura está entre 1.50 y 1.90")
edad = int(input(f"¿Qúe edad tienes? "))
if(edad >= 18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
