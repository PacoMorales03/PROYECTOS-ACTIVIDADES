def suma(n1, n2):
    return n1 + n2
def resta(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2 == 0:
        return 'e'
    else:
        return n1/n2
def pot(n1,n2):
    pot = 1
    for i in range (1,n2+1):
        pot *= n1
    return pot

n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce un numero: "))
print("+ ==> Suma\n- ==> Resta\nx ==> Multiplicación\n/ ==> División\n^ ==> Potencia")
op = input("Introduce la operación a realizar: ")
if(op == "+"):
    print("La suma es:" + suma(n1,n2))
else:
    if(op == "-"):
        print("La resta es:" + resta(n1,n2))
    else:
        if(op == "x"):
            print("La multiplicación es:" + mult(n1,n2))
        else:
            if(op == "/"):
                r = div(n1,n2)
                if r != 'e':
                    print("La división es: " + str(r))
                else:
                    print("Math error")
            else:
                if(op == "^"):
                    
                    print("La potencia es: " + str(pot(n1,n2)))
                else:
                    print("La operación escogida es incorrecta")
                    print("  _____  ")
                    print(" /     \\ ")
                    print("|  o o  |")
                    print("|   ^   |")
                    print(" \\_____/ ")