# ---------------------------| Bibliotecas |---------------------------
import tkinter                                                              # Interfaz gráfica
from paquetes.funciones import *                                            # Funciones para precargar información

# ---------------------------| Precargar información |---------------------------

# Cargar corpus
corpus = leer_corpus('corpus/corpus_filtrado.txt')

# Vector binario
vector_binario = crear_vector_binario(corpus)
vector_frecuencia = crear_vector_frecuencia(corpus)
vector_tfidf = crear_vector_tfidf(corpus)



# ---------------------------| Inicio de interfaz |---------------------------

"""Configuracion de ventana"""
ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.title("Práctica 3 NLP")
ventana.config(bg="white")

"""Contenido de ventana"""

# Crear botones
boton_cargar = tkinter.Button(ventana, text="Cargar archivo", fg="white", bg="green", font="bold")
boton_salir = tkinter.Button(ventana, text="Salir", fg="white", bg="red", font="bold", command=ventana.quit)


# Ubicar botones en interfaz
boton_cargar.place(relx=0.275, rely=0.10, relwidth=0.45, relheight=0.08)
boton_salir.place(relx=0.275, rely=0.82, relwidth=0.45, relheight=0.08)

"""Ejecutar ventana"""
ventana.mainloop()
