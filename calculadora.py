num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
print("+ ==> Suma\n- ==> Resta\nx ==> Multiplicación\n/ ==> División\n^ ==> Potencia")
op = input("Introduce que operacion quieres hacer: ")
if(op == "+"):
    print("La suma es:" + (num1+num2))
else:
    if(op == "-"):
        print("La resta es:" + (num1-num2))
    else:
        if(op == "x"):
            print("La multiplicación es:" + (num1*num2))
        else:
            if(op == "/"):
                if num2 != 0:
                    print("La división es: " + str(num1/num2))
                else:
                    print("Math error")
            else:
                if(op == "^"):
                    pot = 1
                    for i in range (1,num2+1):
                        pot *= num1
                    print("La potencia es: " + str(pot))
                else:
                    print("La operación escogida es incorrecta")
                    print("  _____  ")
                    print(" /     \\ ")
                    print("|  o o  |")
                    print("|   ^   |")
                    print(" \\_____/ ")
                                    