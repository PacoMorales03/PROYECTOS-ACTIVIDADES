import random
print("Debes escoger un número entre el 1 y el 6, si no coincide con el que tiene la bala seguirás jugando.")
print("Si coincide perderás el juego.")
print("¡Buena suerte!")

nums = [1,2,3,4,5,6]
bala = random.randint(1,6) #Se escoge un número aleatorio entre el 1 y el 6
seguir = True
while seguir:
    try:
        num = int(input("Introduce un número entre el 1 y el 6: "))
        if num < 1 or num > 6:
            print("El número debe estar entre 1 y 6.")
        elif num == bala:
            print("Has perdido")
            seguir = False
        else:
            print("De momento sigues vivo, ahora toca elegir de nuevo.")
            nums.remove(num)
            if len(nums) == 1 and nums[0] == bala:
                print("¡Has ganado!")
                seguir = False
    except:
        print("Error con los datos introducidos")