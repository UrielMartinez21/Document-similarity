# ---------------------------| Bibliotecas |---------------------------
import tkinter                                                              # Interfaz gráfica
from paquetes.funciones import *                                            # Funciones para precargar información

# Adrian

# ---------------------------| Precargar información |---------------------------

# Cargar corpus
corpus = leer_corpus('corpus/corpus_filtrado.txt')

# Vector binario
vector_binario = crear_vector_binario(corpus)
vector_frecuencia = crear_vector_frecuencia(corpus)
vector_tfidf = crear_vector_tfidf(corpus)

# ---------------------------| Funciones de interfaz |---------------------------

def opcion_vectorB():
    print("[+]Opción vector binario")
    # --> Preparar texto usuario
    texto_usuario = cargar_archivo()
    texto_normalizado = normalizar_corpus(texto_usuario)
    # --> Crear vector binario
    vectorB_usuario = crear_vector_binario(texto_normalizado)


def opcion_vectorF():
    pass


def opcion_vectorTF():
    pass


def opcion_prueba():
    pass


# ---------------------------| Inicio de interfaz |---------------------------

"""Configuracion de ventana"""
ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.title("Práctica 3 NLP")
ventana.config(bg="white")

"""Contenido de ventana"""

# Crear botones
boton_VB = tkinter.Button(ventana, text="Vector binario", fg="white", bg="green", font="bold", command=opcion_vectorB)
boton_VF = tkinter.Button(ventana, text="Vector frecuencia", fg="white", bg="green", font="bold", command=opcion_vectorF)
boton_VTF = tkinter.Button(ventana, text="Vector TF", fg="white", bg="green", font="bold", command=opcion_vectorTF)
boton_prueba = tkinter.Button(ventana, text="Archivo test", fg="white", bg="blue", font="bold", command=opcion_prueba)
boton_salir = tkinter.Button(ventana, text="Salir", fg="white", bg="red", font="bold", command=ventana.quit)

# Titulo de ventana
nombre_ventana = tkinter.Label(text="Selecciona un tipo", bg="white", font="bold")

# Ubicar titulo en interfaz
nombre_ventana.place(relx=0.25, rely=0.10, relwidth=0.45, relheight=0.08)

# Ubicar botones en interfaz
boton_VB.place(relx=0.275, rely=0.20, relwidth=0.45, relheight=0.08)
boton_VF.place(relx=0.275, rely=0.30, relwidth=0.45, relheight=0.08)
boton_VTF.place(relx=0.275, rely=0.40, relwidth=0.45, relheight=0.08)
boton_prueba.place(relx=0.275, rely=0.60, relwidth=0.45, relheight=0.08)
boton_salir.place(relx=0.275, rely=0.82, relwidth=0.45, relheight=0.08)

"""Ejecutar ventana"""
ventana.mainloop()
