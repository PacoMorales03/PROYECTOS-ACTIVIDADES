import random
import json 
def lanzar_dado():
    dado = {
        1: ["+-------+",
            "|       |",
            "|   O   |",
            "|       |",
            "+-------+"],
        2: ["+-------+",
            "| O     |",
            "|       |",
            "|     O |",
            "+-------+"],
        3: ["+-------+",
            "| O     |",
            "|   O   |",
            "|     O |",
            "+-------+"],
        4: ["+-------+",
            "| O   O |",
            "|       |",
            "| O   O |",
            "+-------+"],
        5: ["+-------+",
            "| O   O |",
            "|   O   |",
            "| O   O |",
            "+-------+"],
        6: ["+-------+",
            "| O   O |",
            "| O   O |",
            "| O   O |",
            "+-------+"]
    }
    resultado = random.randint(1, 6)
    for linea in dado[resultado]:
        print(linea)
    return resultado

def combate(vidaPJ, atqPJ):
    enemigo = random.choice(enemigos)
    print(f"Has encontrado un enemigo de tipo {enemigo}")
    enemigos_caracteristicas = {
        "orco": {"vida": 100, "ataque": 50},
        "goblin": {"vida": 50, "ataque": 15},
        "arquero": {"vida": 80, "ataque": 40},
        "dios": {"vida": 1000, "ataque": 1000}
    }
    vida_enemigo = enemigos_caracteristicas[enemigo]["vida"]
    ataque_enemigo = enemigos_caracteristicas[enemigo]["ataque"]
    while vidaPJ > 0 and vida_enemigo > 0:
        input("Presiona enter para lanzar el dado")
        dado = lanzar_dado()
        if dado >= 1 and dado <= 3:
            atqPJ += 50
        elif dado >= 4 and dado <= 6:
            atqPJ += 100
        print(f"Tu ataque es: {atqPJ}")
        vida_enemigo -= atqPJ
        print(f"El ataque del enemigo es: {ataque_enemigo}")
        vidaPJ -= ataque_enemigo
        print(f"Tu vida actual es: {vidaPJ}HP")
        print(f"La vida del enemigo es: {vida_enemigo}HP")
    
    if vidaPJ > 0:
        print("Has ganado el combate!")
        return True
    else:
        print("Has perdido el combate...")
        return False

vidaPJ = 100
atqPJ = 100
eventos = ["enemigo","cofre","trampa","precipicio","salida"]
enemigos = ["orco","goblin","arquero","dios"]
cofres = ["vida","ataque","trampa"]
seguir = True
vidaPJ = 100
atqPJ = 100
while seguir:
    if vidaPJ > 0:
        jugada = input("Elige a que dirección ir: izquierda, derecha o adelante: ")
        if jugada == "adelante" or jugada == "izquierda" or jugada == "derecha":
            evento = random.choice(eventos)
            if evento == "enemigo":
                if not combate(vidaPJ,atqPJ):
                    seguir = False
            elif evento == "cofre":
                cofre = random.choice(cofres)
                if(cofre == "vida"):
                    print("Has encontrado un cofre de vida")
                    vidaPJ += 50
                    print(f"Tu vida actual es: {vidaPJ}HP")
                elif(cofre == "ataque"):
                    print("Has encontrado un cofre de ataque")
                    atqPJ += 50
                    print(f"Tu ataque actual es: {atqPJ}")
                else:
                    print("Has encontrado un cofre trampa")
                    vidaPJ -= 30
                    print(f"Tu vida actual es: {vidaPJ}HP")
            elif evento == "trampa":
                print("¡Oh no! Has caido en una trampa")
                vidaPJ -= 30
                print(f"Tu vida actual es: {vidaPJ}HP")
            elif evento == "precipicio":
                print("¡Oh no! Has caido en un precipicio")
                vidaPJ -= 20
                print(f"Tu vida actual es: {vidaPJ}HP")
            else:
                print("Has conseguido escapar")
                seguir = False
        else:
            print("Dirección incorrecta")
    else:
        print("Has muerto")
        seguir = False
        with open("datos.json", "w") as archivo:
            json.dump(vidaPJ, archivo, indent = 4)
