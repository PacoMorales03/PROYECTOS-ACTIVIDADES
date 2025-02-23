def sumar(*arg):
    return sum(arg)
op = 0
r = 0
leido = False
while(op.lower() != 's'):
    op = input("Introduce un número o s para salir: ")
    if op.isdigit():
        r = sumar(r,int(op))
        leido = True
    elif op.lower() != 's':
        print("Dato introducido incorrecto")
if leido:
    print(f"La suma total es: {r}")