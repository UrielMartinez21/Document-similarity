# ---------------------------| Bibliotecas |---------------------------
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer    # Vectorizador
import tkinter                                                                  # Interfaz gráfica
from paquetes.funciones import *                                                # Funciones para precargar información

# ---------------------------| Precargar información |---------------------------

# Cargar corpus
corpus = leer_corpus('corpus/corpus_filtrado.txt')

# Vector binario
vectorizador_binario = CountVectorizer(binary=True, token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
X = vectorizador_binario.fit_transform(corpus)
vector_binario = X.toarray()

# Vector frecuencia
vectorizador_frecuencia = CountVectorizer(token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
X = vectorizador_frecuencia.fit_transform(corpus)
vector_frecuencia = X.toarray()

# Vector tf-idf
vectorizador_tfidf = TfidfVectorizer(token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
X = vectorizador_tfidf.fit_transform(corpus)
vector_tfidf = X.toarray()


# ---------------------------| Funciones de interfaz |---------------------------

def opcion_vectorB():
    """
    Función para crear vector binario
    return: lista
    """
    # --> Preparar texto usuario
    texto_usuario = cargar_archivo()
    texto_normalizado = normalizar_corpus(texto_usuario)
    # --> Crear vector binario
    vectorB_usuario = vectorizador_binario.transform(texto_normalizado).toarray()


def opcion_vectorF():
    """
    Función para crear vector frecuencia
    return: lista
    """
    # --> Preparar texto usuario
    texto_usuario = cargar_archivo()
    texto_normalizado = normalizar_corpus(texto_usuario)
    # --> Crear vector frecuencia
    vectorF_usuario = vectorizador_frecuencia.transform(texto_normalizado).toarray()


def opcion_vectorTF():
    """
    Función para crear vector tf-idf
    return: lista
    """
    # --> Preparar texto usuario
    texto_usuario = cargar_archivo()
    texto_normalizado = normalizar_corpus(texto_usuario)
    # --> Crear vector tf-idf
    vectorTF_usuario = vectorizador_tfidf.transform(texto_normalizado).toarray()


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
boton_salir = tkinter.Button(ventana, text="Salir", fg="white", bg="red", font="bold", command=ventana.quit)

# Titulo de ventana
nombre_ventana = tkinter.Label(text="Selecciona un tipo", bg="white", font="bold")

# Ubicar titulo en interfaz
nombre_ventana.place(relx=0.25, rely=0.10, relwidth=0.45, relheight=0.08)

# Ubicar botones en interfaz
boton_VB.place(relx=0.275, rely=0.20, relwidth=0.45, relheight=0.08)
boton_VF.place(relx=0.275, rely=0.30, relwidth=0.45, relheight=0.08)
boton_VTF.place(relx=0.275, rely=0.40, relwidth=0.45, relheight=0.08)
boton_salir.place(relx=0.275, rely=0.82, relwidth=0.45, relheight=0.08)

"""Ejecutar ventana"""
ventana.mainloop()
