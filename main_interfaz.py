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
    print("[+]Inicia la ejecución...")
    # --> Borrar el contenido actual del widget de texto
    texto_resultados.delete('1.0', tkinter.END)
    try:
        # --> Preparar texto usuario
        texto_usuario = cargar_archivo()
        texto_normalizado = normalizar_corpus(texto_usuario)
        # --> Crear vector binario
        vectorB_usuario = vectorizador_binario.transform(texto_normalizado).toarray()
        # --> Determinar similitud
        lista = [(cosine(vector_binario[i], vectorB_usuario[0]), i) for i in range(len(vector_binario))]
        # --> Primeros 10 documentos más similares
        resultados = sorted(lista, reverse=True)[:10]
        # --> Multiplicar por 100 para obtener porcentaje
        resultados = [f"{i+1}) {round(resultados[i][0] * 100, 2)}%    Documento: {resultados[i][1]}" for i in range(len(resultados))]
        # --> Agregar cada valor de la lista en un nuevo renglón
        for resultado in resultados:
            texto_resultados.insert(tkinter.END, f'{resultado}\n')
    except:
        print("[-]Se cancelo la ejecución")


def opcion_vectorF():
    """
    Función para crear vector frecuencia
    return: lista
    """
    print("[+]Inicia la ejecución...")
    # --> Borrar el contenido actual del widget de texto
    texto_resultados.delete('1.0', tkinter.END)
    try:
        # --> Preparar texto usuario
        texto_usuario = cargar_archivo()
        texto_normalizado = normalizar_corpus(texto_usuario)
        # --> Crear vector frecuencia
        vectorF_usuario = vectorizador_frecuencia.transform(texto_normalizado).toarray()
        # --> Determinar similitud
        lista = [(cosine(vector_frecuencia[i], vectorF_usuario[0]), i) for i in range(len(vector_frecuencia))]
        # --> Primeros 10 documentos más similares
        resultados = sorted(lista, reverse=True)[:10]
        # --> Multiplicar por 100 para obtener porcentaje
        resultados = [f"{i+1}) {round(resultados[i][0] * 100, 2)}%    Documento: {resultados[i][1]}" for i in range(len(resultados))]
        # --> Agregar cada valor de la lista en un nuevo renglón
        for resultado in resultados:
            texto_resultados.insert(tkinter.END, f'{resultado}\n')
        print("[+]Termino la ejecución")
    except:
        print("[-]Se cancelo la ejecución")


def opcion_vectorTF():
    """
    Función para crear vector tf-idf
    return: lista
    """
    print("[+]Inicia la ejecución...")
    # --> Borrar el contenido actual del widget de texto
    texto_resultados.delete('1.0', tkinter.END)
    try:
        # --> Preparar texto usuario
        texto_usuario = cargar_archivo()
        texto_normalizado = normalizar_corpus(texto_usuario)
        # --> Crear vector tf-idf
        vectorTF_usuario = vectorizador_tfidf.transform(texto_normalizado).toarray()
        # --> Determinar similitud
        lista = [(cosine(vector_tfidf[i], vectorTF_usuario[0]), i) for i in range(len(vector_tfidf))]
        # --> Primeros 10 documentos más similares
        resultados = sorted(lista, reverse=True)[:10]
        # --> Multiplicar por 100 para obtener porcentaje
        resultados = [f"{i+1}) {round(resultados[i][0] * 100, 2)}%    Documento: {resultados[i][1]}" for i in range(len(resultados))]
        # --> Agregar cada valor de la lista en un nuevo renglón
        for resultado in resultados:
            texto_resultados.insert(tkinter.END, f'{resultado}\n')
        print("[+]Termino la ejecución")
    except:
        print("[-]Se cancelo la ejecución")


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

# Crear un widget de texto para mostrar los resultados
texto_resultados = tkinter.Text(ventana, bg="white", font=("Arial", 12))
texto_resultados.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.35)

# Titulo de ventana
nombre_ventana = tkinter.Label(text="Selecciona un tipo", bg="white", font="bold", justify="center")

# Ubicar titulo en interfaz
nombre_ventana.place(relx=0.25, rely=0.05, relwidth=0.45, relheight=0.08)

# Ubicar botones en interfaz
boton_VB.place(relx=0.275, rely=0.15, relwidth=0.45, relheight=0.08)
boton_VF.place(relx=0.275, rely=0.25, relwidth=0.45, relheight=0.08)
boton_VTF.place(relx=0.275, rely=0.35, relwidth=0.45, relheight=0.08)
boton_salir.place(relx=0.275, rely=0.90, relwidth=0.45, relheight=0.08)

"""Ejecutar ventana"""
ventana.mainloop()
