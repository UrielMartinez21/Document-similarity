from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer # Vectorizador      
import tkinter                                                              # Interfaz gráfica
from tkinter import filedialog                                              # Cuadro de dialogo
from paquetes.funciones import *                                            # Funciones para precargar información

# --> Precargar información

# Cargar corpus
corpus = leer_corpus('corpus/corpus_filtrado.txt')

# Vector binario
vectorizador_binario = CountVectorizer(binary=True, token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
X = vectorizador_binario.fit_transform(corpus)
print('Representación vectorial binarizada')
print(X.toarray())

# Vector de frecuencia
vectorizador_frecuencia = CountVectorizer(token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
X = vectorizador_frecuencia.fit_transform(corpus)
print('Representación vectorial por frecuencia')
print(X.toarray())

# Vector TF-IDF
vectorizador_tfidf = TfidfVectorizer(token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
X = vectorizador_tfidf.fit_transform(corpus)
print('Representación vectorial tf-idf')
print(X.toarray())




# --> Variables globales
noticias_seleccionadas = None


# --> Funciones

def cargar_archivo():
    """Función para cargar archivos txt"""
    ruta_archivo = filedialog.askopenfilename(title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"),))
    print(f'[+]La ruta es: {ruta_archivo}')
    with open(ruta_archivo, "r", encoding="utf-8") as informacion:
        noticias_seleccionadas = informacion.read().split('\n')
    return noticias_seleccionadas


# --> Inicio de interfaz

"""Configuracion de ventana"""
ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.title("Práctica 3 NLP")
ventana.config(bg="white")

"""Contenido de ventana"""

# Crear botones
boton_cargar = tkinter.Button(ventana, text="Cargar archivo", fg="white", bg="green", font="bold", command=cargar_archivo)
boton_salir = tkinter.Button(ventana, text="Salir", fg="white", bg="red", font="bold", command=ventana.quit)


# Ubicar botones en interfaz
boton_cargar.place(relx=0.275, rely=0.10, relwidth=0.45, relheight=0.08)
boton_salir.place(relx=0.275, rely=0.82, relwidth=0.45, relheight=0.08)

"""Ejecutar ventana"""
ventana.mainloop()
