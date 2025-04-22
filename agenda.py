agenda ={}

import time
import sys

#funcion para imprimir lento cada caracter con un tiempo de espera entre cada uno
def imprimir_lento(texto, velocidad=0.045):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()  # Imprime una nueva línea al final de cada impresion

# funcion para imprimir el menu de opciones

def menu():
    imprimir_lento("Bienvenido a tu agenda personal! ", 0.045)
    imprimir_lento("Que accion quiere llevar a cabo? ", 0.045)
    imprimir_lento("---Menu--- ", 0.045)
    imprimir_lento("1. Agregar contacto ", 0.045)
    imprimir_lento("2. Buscar contactos por nombre ", 0.045)
    imprimir_lento("3. Mostrar contactos de tu agenda ", 0.045)
    imprimir_lento("4. salir", 0.045)

## funcion para agregar un contacto a la agenda

def agregar_contacto():
    contacto = input("ingrese el nombre del contacto: ").lower()
    imprimir_lento("¿Quieres agregar un numero telefonico? (si/no)" , 0.045)
    respuesta = input().lower()
    if respuesta == "si":
        telefono = input("ingrese el numero telefonico del contacto: ")
        agenda[contacto + " " + telefono] = contacto + " " + telefono
        imprimir_lento(f"el contacto {contacto} con el numero {telefono} se ha agregado correctamente! Vaya agenda estas creando!", 0.045)
    else:
        agenda[contacto] = contacto
    imprimir_lento(f"el contacto {contacto} se ha agregado correctamente! Vaya agenda estas creando!", 0.045)


#  funcion que mostrara los contactos almacenados en la agenda
def mostrar_contactos():
        if len(agenda) == 0:
            imprimir_lento ("no has agregado ningun contacto a tu agenda :(" \
            " Intenta agregar uno!" , 0.045)
            imprimir_lento("redirigiendo al menu..." , 0.045)
        else:
            imprimir_lento ("los contactos agregados en tu agenda son:", 0.045)
            for i in agenda:
             imprimir_lento (i + "!" , 0.045)
            imprimir_lento("tienes muchos contactos...", 0.045)
            imprimir_lento("redirigiendo al menu...", 0.045)

#funcion para hacer la busqueda de un contacto en la agenda

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto que desea buscar: ").lower()
    encontrados = []

    for contacto in agenda:
        if nombre in contacto.lower():
            encontrados.append(contacto)

    if encontrados:
        imprimir_lento("Contactos encontrados:", 0.045)
        for contacto in encontrados:
            imprimir_lento(f"- {contacto}", 0.045)
    else:
        imprimir_lento(f"No se encontraron contactos que coincidan con '{nombre}'.", 0.045)

while True:
    menu()
    accion = input("que accion desea llevar a cabo? (1, 2, 3 o 4?)")

    if accion == "1":
        agregar_contacto()

    elif accion == "2":
        buscar_contacto()

    elif accion == "3":
        mostrar_contactos()

    elif accion == "4":
        imprimir_lento("saliendo del programa..." , 0.045)
        agenda.clear()
        imprimir_lento("Gracias por usar el programa!" , 0.045)
        break

    else:
        imprimir_lento("accion no valida, intente de nuevo con un numero valido (1, 2, 3 o 4)", 0.045)
        imprimir_lento("redirigiendo al menu...", 0.045)