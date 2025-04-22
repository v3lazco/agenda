import tkinter as tk
import json

# Variables globales
agenda = {}
ventana = tk.Tk()

# Configuración inicial de la ventana
ventana.title("Agenda de Contactos")
ventana.geometry("420x500")
ventana.config(bg="#0E0E0E")

# Funciones para manejar los datos almacenados
def cargar_agenda():
    global agenda
    try:
        with open("agenda.json", "r") as archivo:
            agenda = json.load(archivo)
    except FileNotFoundError:
        agenda = {}

def guardar_agenda():
    with open("agenda.json", "w") as archivo:
        json.dump(agenda, archivo)

# Funciones para el uso de los botones

def guardar_contacto():
    nombre = entrada_nombre.get()
    numero = entrada_numero.get()
    if nombre and numero:
        agenda[nombre] = numero
        guardar_agenda()
        actualizar_mensaje(f"Contacto '{nombre}' agregado.")
        limpiar_entradas()
        frame_agregar.pack_forget()
        mostrar_botones()
    else:
        actualizar_mensaje("Completa ambos campos.")

def buscar_contacto():
    nombre_buscar = entrada_buscar.get().lower()
    resultados = [f"{nombre}: {numero}" for nombre, numero in agenda.items() if nombre_buscar in nombre.lower() or nombre_buscar in numero]

    if len(nombre_buscar) >= 1:
        if resultados:
            actualizar_mensaje("Resultados encontrados:\n" + "\n".join(resultados))
        else:
            actualizar_mensaje("No se encontraron contactos.")
    else:
        actualizar_mensaje("Por favor, ingresa al menos un carácter.")

    limpiar_entradas()
    ocultar_campos_buscar()
    mostrar_botones()


def actualizar_mensaje(texto):
    etiqueta_mensaje.config(text=texto)

def eliminar_contacto(nombre_buscar):
    nombre_buscar = nombre_buscar.lower()
    resultados = [(nombre, numero) for nombre, numero in agenda.items() if nombre_buscar in nombre.lower() or nombre_buscar in numero]

    if len(nombre_buscar) >= 1:
        if resultados:
            actualizar_mensaje("Resultados encontrados:\n" + "\n".join([f"{nombre}: {numero}" for nombre, numero in resultados]))
            boton_eliminar_contacto.config(command=lambda: confirmar_eliminacion(resultados[0][0]))
            boton_eliminar_contacto.pack(pady=10)
        else:
            actualizar_mensaje("No se encontraron contactos.")
    else:
        actualizar_mensaje("Por favor, ingresa al menos un carácter.")

def confirmar_eliminacion(nombre):
    if nombre in agenda:
        del agenda[nombre]
        actualizar_mensaje(f"Contacto '{nombre}' eliminado.")
        guardar_agenda()
        limpiar_entradas()
        ocultar_campos_eliminar()
        mostrar_botones()

# funciones para mostrar y ocultar textos y botones

def mostrar_eliminar_contacto():
    ocultar_todo()
    frame_eliminar.pack(pady=20)

def mostrar_lista_contactos():
    ocultar_todo()
    if agenda:
        contactos = "\n".join([f"{nombre}: {numero}" for nombre, numero in agenda.items()])
        actualizar_mensaje("Lista de contactos:\n" + contactos)
    else:
        actualizar_mensaje("No hay contactos en la agenda.")
    mostrar_botones()

def mostrar_campos_agregar():
    ocultar_todo()
    frame_agregar.pack(pady=20)

def mostrar_buscar_contacto():
    ocultar_todo()
    frame_buscar.pack(pady=20)

def mostrar_botones():
    frame_botones.pack(pady=20)

def ocultar_todo():
    ocultar_botones()
    ocultar_campos_agregar()
    ocultar_campos_buscar()
    ocultar_campos_eliminar()

def ocultar_campos_agregar():
    frame_agregar.pack_forget()

def ocultar_campos_buscar():
    frame_buscar.pack_forget()

def ocultar_campos_eliminar():
    frame_eliminar.pack_forget()
    boton_eliminar_contacto.pack_forget()

def ocultar_botones():
    frame_botones.pack_forget()

# funcion para limpiar entradas de texto

def limpiar_entradas():
    entrada_nombre.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)
    entrada_buscar.delete(0, tk.END)
    entrada_eliminar.delete(0, tk.END)

# Widgets principales
etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido a tu agenda personal!",  font=("Arial", 14, "bold") , bg="#0E0E0E", fg="white")
etiqueta_bienvenida.pack(pady=5)

etiqueta_pregunta = tk.Label(ventana, text="¿Qué quieres hacer con tu agenda?", font=("Arial", 12) , bg="#0E0E0E", fg="white")
etiqueta_pregunta.pack(pady=5)

etiqueta_mensaje = tk.Label(ventana, text="", font=("Arial", 11, "italic" , "bold"), bg="#0E0E0E", fg="white")
etiqueta_mensaje.pack(pady=10)

# Frame de botones principales de la interfaz
frame_botones = tk.Frame(ventana, bg="white", padx=20, pady=20, bd=2, relief="ridge")
frame_botones.pack(pady=20)

boton_agregar = tk.Button(frame_botones, text="Agregar contacto", command=mostrar_campos_agregar, width=25, bg="#34495E", fg="white")
boton_buscar = tk.Button(frame_botones, text="Buscar contacto", command=mostrar_buscar_contacto, width=25, bg="#34495E", fg="white")
boton_mostrar = tk.Button(frame_botones, text="Mostrar lista de contactos", command=mostrar_lista_contactos, width=25, bg="#34495E", fg="white")
boton_eliminar = tk.Button(frame_botones, text="Eliminar contacto", command=mostrar_eliminar_contacto, width=25, bg="#34495E", fg="white")
boton_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit, width=25, bg="#34495E", fg="white")

for boton in [boton_agregar, boton_buscar, boton_mostrar, boton_eliminar, boton_salir]:
    boton.pack(pady=5)

# Frame para agregar contacto
frame_agregar = tk.Frame(ventana, bg="#ffffff", padx=20, pady=20, bd=2, relief="ridge")
tk.Label(frame_agregar, text="Agregar contacto", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=(0, 10))
tk.Label(frame_agregar, text="Nombre:", bg="#ffffff").pack(anchor="w")
entrada_nombre = tk.Entry(frame_agregar, width=30)
entrada_nombre.pack(pady=5)
tk.Label(frame_agregar, text="Número:", bg="#ffffff").pack(anchor="w")
entrada_numero = tk.Entry(frame_agregar, width=30)
entrada_numero.pack(pady=5)
tk.Button(frame_agregar, text="Guardar", command=guardar_contacto, bg="#34495E", fg="black").pack(pady=10)

# Frame para buscar contacto
frame_buscar = tk.Frame(ventana, bg="#ffffff", padx=20, pady=20, bd=2, relief="ridge")
tk.Label(frame_buscar, text="Buscar contacto", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=(0, 10))
tk.Label(frame_buscar, text="Nombre o número:", bg="#ffffff").pack(anchor="w")
entrada_buscar = tk.Entry(frame_buscar, width=30)
entrada_buscar.pack(pady=5)
boton_buscar_confirmar = tk.Button(frame_buscar, text="Buscar", command=buscar_contacto, bg="#34495E", fg="white")
boton_buscar_confirmar.pack(pady=10)

# Frame para eliminar contacto
frame_eliminar = tk.Frame(ventana, bg="#ffffff", padx=20, pady=20, bd=2, relief="ridge")
tk.Label(frame_eliminar, text="Eliminar contacto", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=(0, 10))
tk.Label(frame_eliminar, text="Nombre o número:", bg="#ffffff").pack(anchor="w")
entrada_eliminar = tk.Entry(frame_eliminar, width=30)
entrada_eliminar.pack(pady=5)
boton_eliminar_buscar = tk.Button(frame_eliminar, text="Buscar para eliminar", command=lambda: eliminar_contacto(entrada_eliminar.get()), bg="#34495E", fg="white")
boton_eliminar_buscar.pack(pady=10)

boton_eliminar_contacto = tk.Button(frame_eliminar, text="Confirmar eliminación", bg="#ff073a", fg="black")

# Cargar datos y ejecutar
cargar_agenda()
ventana.mainloop()

