import json

def agregar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el teléfono del contacto: ")
    email = input("Introduce el email del contacto: ")
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    contactos.append(contacto)

def mostrar_contactos():
    print("Contactos registrados:")
    for contacto in contactos:
        print(f"  {contacto['nombre']}: {contacto['telefono']} - {contacto['email']}")

def buscar_contacto():
    nombre = input("Introduce el nombre del contacto a buscar: ")
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            print(f"  {contacto['nombre']}: {contacto['telefono']} - {contacto['email']}")
            return
    print("Error: No se encontró el contacto.")

def modificar_contacto():
    nombre = input("Introduce el nombre del contacto a modificar: ")
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            telefono = input("Introduce el nuevo teléfono del contacto: ")
            email = input("Introduce el nuevo email del contacto: ")
            contacto["telefono"] = telefono
            contacto["email"] = email
            print(f"  {contacto['nombre']}: {contacto['telefono']} - {contacto['email']}")
            return
    print("Error: No se encontró el contacto.")

def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            contactos.pop(contacto)
            print(f"Se eliminó el contacto {nombre}")
            return
    print("Error: No se encontró el contacto.")

def cargar_contactos():
    try:
        with open("contactos.json", "r") as archivo:
            contactos = json.load(archivo)
            return contactos
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

def guardar_contactos():
    with open("contactos.json","w") as archivo:
        json.dump(contactos, archivo, indent = 4)

contactos = cargar_contactos()
seguir = True
while seguir:
    print("\nMenú de opciones:")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

    op = input("Introduce la opción deseada: ")
    if op == "1":
        agregar_contacto()
    elif op == "2":
        mostrar_contactos()
    elif op == "3":
        buscar_contacto()
    elif op == "4":
        modificar_contacto()
    elif op == "5":
        eliminar_contacto()
    elif op == "6":
        guardar_contactos()
        print("Hasta luego!")
        seguir = False
    else:
        print("Opción inválida. Por favor, introduce una opción válida.")