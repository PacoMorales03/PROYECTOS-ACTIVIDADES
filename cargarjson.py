import json

def cargar_partida():
    try:
        with open("partida.json", "r") as archivo:
            partida = json.load(archivo)
            return partida
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    
